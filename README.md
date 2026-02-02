# Productivity Core API

A backend-only RESTful API built with **Django** and **Django REST Framework** for managing personal productivity features such as **Notes, ToDo's, Reminders, Categories, and Priorities**.

This project is designed as a scalable, modular backend that can power web or mobile productivity applications.

## 🚀 Features
- CRUD APIs for **Notes**, **ToDo's**, and **Reminders**
- RESTful API architecture
- Categories & Tags
- Pagination support
- Search across title and description
- Filtering by:
  - Category
  - Completion status
  - Created date range
  - Priority
- Flexible ordering (date, title, priority)
- Django ORM & SQLite

## 🛠 Tech Stack
- Python
- Django
- Django REST Framework
- SQLite

## 📌 Planned Features
- User authentication & authorization (JWT)
- User-specific data isolation
- Frontend integration
- Notification system

## ⚙️ Setup Instructions

```bash
git clone https://github.com/ikshu7/Productivity-Core-API.git
cd Productivity-Core-API
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
