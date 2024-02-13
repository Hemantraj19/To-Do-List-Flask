# Flask ToDo App

This is a Flask web application for managing ToDo tasks. Users can register, log in, add tasks, mark tasks as done, set deadlines, and customize task colors.

## Features

- **User Authentication**: Users can register and log in securely.
- **CRUD Operations**: Users can create, read, update, and delete tasks.
- **Task Management**: Users can mark tasks as done, set deadlines, and customize task colors.
- **Responsive Design**: Utilizes Bootstrap for a responsive and visually appealing interface.

## Setup and Usage

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Access the application in your web browser at `http://localhost:5000`.

## File Structure

- `app.py`: Main Flask application file containing routes and database setup.
- `form.py`: Contains form classes for user login and registration.
- `templates/`: Directory containing HTML templates for rendering pages.
- `static/`: Directory containing static files such as CSS stylesheets and JavaScript scripts.
- `todo.db`: SQLite database file for storing tasks and user information.

## Dependencies

- Flask: Micro web framework for Python.
- Flask-SQLAlchemy: Flask extension for SQLAlchemy database integration.
- Flask-Login: Provides user session management for Flask applications.
- Flask-Bootstrap: Integration of Bootstrap framework with Flask.
- Werkzeug: Provides utilities for web development with Flask.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- scrypt: Password-based key derivation function used for password hashing.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
