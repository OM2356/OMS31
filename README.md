# Flask To-Do Web Application

A secure, relational database-backed To-Do list web application built with Flask, Flask-SQLAlchemy, and Flask-Login.

## Features

*   **User Authentication**: Secure user registration and login functionality.
*   **Password Hashing**: Secure data protection using `werkzeug.security` (PBKDF2 with SHA256).
*   **Relational Database**: Persistent SQLite database storing users and their respective tasks.
*   **Protected Routes**: Personalized task dashboards accessible only to logged-in users.

## Prerequisites

Ensure you have Python 3.8 or higher installed on your system.

## Project Structure

```text
├── app.py            # Main application script & database models
├── todo.db           # SQLite database file (generated automatically)
└── templates/        # UI layout folders
    ├── index.html    # Logged-in user task dashboard
    ├── login.html    # User login panel
    └── register.html # New user registration panel
```

## Setup Instructions

### 1. Clone or Create the Project Directory
Navigate to your project workspace directory in your terminal:
```bash
cd path/to/your/project
```

### 2. Set Up a Virtual Environment (Recommended)
Isolate your project dependencies by running:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install all required package libraries at once:
```bash
pip install Flask Flask-SQLAlchemy Flask-Login
```

### 4. Initialize the RDBMS File
Run the application once to automatically build the SQLite `todo.db` database schema:
```bash
python app.py
```

### 5. Access the Web App
Open your web browser and navigate to the local hosting URL:
```text
127.0.0
```

## Security Note

Before deploying this web application to a live cloud server, remember to change the `SECRET_KEY` property inside `app.py` to a long, randomized string to safeguard user login session cookies.
