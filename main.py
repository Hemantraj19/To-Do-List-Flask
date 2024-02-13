from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime
from flask_login import UserMixin, LoginManager, login_user, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bootstrap import Bootstrap5
from form import LoginForm, RegisterForm

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = "aejrfdilvuhkdsdfjgdfgier"

Base = declarative_base()

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db.init_app(app)

Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


class ToDo(db.Model):
    __tablename__ = "list"
    id = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)
    date = Column(String, nullable=True)
    task_done = Column(Integer, nullable=False, default=0)
    color = Column(String, nullable=True, default="#E7E7E7")
    user_id = Column(Integer, ForeignKey("user.id"))


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    list = db.relationship("ToDo", backref="user", lazy=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    if current_user.is_authenticated:
        todo_list = (
            db.session.execute(
                db.select(ToDo)
                .where(ToDo.user_id == current_user.id)
                .order_by(ToDo.task_done)
            )
            .scalars()
            .all()
        )
    else:
        todo_list = (
            db.session.execute(
                db.select(ToDo).where(ToDo.user_id == None).order_by(ToDo.task_done)
            )
            .scalars()
            .all()
        )
    return render_template("index.html", todo_list=todo_list, current_user=current_user)


@app.route("/add", methods=["POST"])
def add_task():
    new_todo = ToDo(
        task=request.form.get("task"),
        user_id=current_user.id if current_user.is_authenticated else None,
    )
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/pick-color/<int:todo_id>", methods=["POST"])
def pick_color(todo_id):
    color = request.form.get("picked-color")
    print(color)
    todo = db.get_or_404(ToDo, todo_id)
    todo.color = color
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = db.get_or_404(ToDo, todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/checked/<int:todo_id>")
def checkbox(todo_id):
    todo = db.get_or_404(ToDo, todo_id)
    todo.task_done = 1
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/date-picked/<int:todo_id>", methods=["POST"])
def date_picked(todo_id):
    input_date = request.form.get("date-pick")
    # input_date_object = datetime.strptime(input_date, "%Y-%m-%d")
    # current_date = datetime.now()
    # due_days = (input_date_object - current_date).days
    todo = db.get_or_404(ToDo, todo_id)
    todo.date = input_date
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if not user:
            flash("Wrong username or password")
            return redirect(url_for("login"))
        elif not check_password_hash(user.password, password):
            flash("Wrong username or password")
        else:
            login_user(user)
            return redirect(url_for("home"))
    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        new_user = User(
            name=register_form.name.data,
            email=register_form.email.data,
            password=generate_password_hash(
                register_form.password.data, method="scrypt", salt_length=8
            ),
        )
        db.session.add(new_user)
        db.session.commit()
        flash("User Registered Successfully.")
        return redirect(url_for("login"))
    return render_template("register.html", register_form=register_form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
