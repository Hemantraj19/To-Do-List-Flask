from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import declarative_base

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = "aejrfdilvuhkdsdfjgdfgier"

Base = declarative_base()

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db.init_app(app)


class ToDo(db.Model):
    __tablename__ = "list"
    id = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)
    date = Column(String, nullable=True)
    color = Column(String, nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    todo_list = db.session.execute(db.select(ToDo)).scalars().all()
    return render_template("index.html", list=todo_list)


@app.route("/add", methods=["POST"])
def add_task():
    new_todo = ToDo(task=request.form.get("task"))
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
