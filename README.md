# 🚀 Flask To-Do Web Application

<div align="center">

![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![Python](https://img.shields.io/badge/Python-Programming-blue?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

✨ Secure • Fast • Responsive • Database Powered ✨

</div>

---

# 📝 About The Project

Flask To-Do Web Application is a secure and responsive task management system developed using Flask, Flask-SQLAlchemy, and Flask-Login.

The application allows users to register securely, log in to personalized dashboards, and manage daily tasks with database-backed storage using SQLite.

---

# 🔥 Features

## 🔐 Authentication System
- Secure User Registration
- Login & Logout Functionality
- Password Hashing using Werkzeug Security
- Protected User Sessions

---

## 📋 Task Management
- Create Tasks
- Update Tasks
- Delete Tasks
- Personalized Task Dashboard

---

## 🗄️ Relational Database Management System (RDBMS)

The application uses **SQLite**, a lightweight relational database management system, for storing users and tasks securely.

### ✨ Database Features

- Structured Relational Database
- Persistent Data Storage
- User-Task Relationship Mapping
- Automatic Table Creation
- Lightweight & Fast Performance

---

# 📊 Database Structure

```text
Users Table
│
├── id
├── username
├── email
└── password_hash

Tasks Table
│
├── id
├── task
├── completed
└── user_id (Foreign Key)
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend Programming |
| Flask | Web Framework |
| Flask-SQLAlchemy | ORM Database Handling |
| Flask-Login | User Authentication |
| SQLite | Relational Database |
| HTML/CSS | Frontend UI |

---

# 📂 Project Structure

```text
📦 Flask-Todo-App
│
├── 📄 app.py
├── 📄 todo.db
│
├── 📁 templates
│   ├── index.html
│   ├── login.html
│   └── register.html
│
├── 📁 static
│   ├── style.css
│   └── script.js
│
└── 📄 README.md
```

---

# ⚡ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/flask-todo-app.git
```

---

## 2️⃣ Open Project Folder

```bash
cd flask-todo-app
```

---

## 3️⃣ Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install Flask Flask-SQLAlchemy Flask-Login
```

---

## 5️⃣ Run Application

```bash
python app.py
```

---

# 🌐 Open In Browser

```text
http://127.0.0.1:5000
```

---

# 🔒 Security Features

✅ Password Hashing  
✅ Session Protection  
✅ Secure Authentication  
✅ Protected Routes  
✅ Database Security  

---

# 🎨 UI Features

✨ Responsive Design  
🌙 Modern Clean Interface  
⚡ Smooth User Experience  
📱 Mobile-Friendly Layout  

---

# 🚀 Future Improvements

- Dark Mode
- Task Categories
- Due Dates & Reminders
- Email Notifications
- Cloud Database Integration
- REST API Support

---

# 👨‍💻 Developer

Developed by Omkar Sathe 🚀

---

# 📜 License

This project is licensed under the MIT License.

---

<div align="center">

## ⭐ Star This Repository If You Like It

Made with ❤️ using Flask & Python

</div>
