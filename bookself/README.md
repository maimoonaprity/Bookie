# 📚 Bookself API

A **read-only RESTful backend API** built with **Django & Django REST Framework** for serving book-related data.  
Administrative CRUD operations are handled securely through the **Django Admin Panel**.

This project is developed as part of the **Antripe Internship Program (Backend Developer – Python) – 2025**.

---

## 📌 Project Information

- **Project Name:** Bookself API  
- **Repository:** https://github.com/maimoonaprity/Bookie/tree/newv/bookself 
- **Submitted By:** Maimoona Prity Joarder 
- **Submitted To:** Ekramul Islam Shadik  
- **Program:** Antripe Internship Program (Backend Developer – Python) – 2025  

---

## 🧾 Project Overview

Bookself API exposes **public, read-only endpoints** to retrieve information about:

- Books  
- Authors  
- Categories  
- Publishers  

All **create, update, and delete (CRUD)** operations are **restricted to the Django Admin Panel**, ensuring controlled data management and improved security.

This architecture reflects a real-world scenario where:
- **Users** can only view data  
- **Admins** manage content internally  

---

## 🔐 Access Control Design

| Role | Access |
|-----|-------|
| Public API Users | Read-only (GET) |
| Admin (Django Admin) | Full CRUD |

✔ Public endpoints allow **safe data consumption**  
✔ Admin panel ensures **data integrity and control**

---

## 🚀 Features

✔ Read-only REST APIs for books, authors, categories, and publishers  
✔ Admin-only CRUD operations via Django Admin  
✔ Optimized queries using Django ORM  
✔ Clean serialization using Django REST Framework  
✔ Browsable API interface for testing  

---

## 🛠 Tech Stack

- **Language:** Python  
- **Framework:** Django  
- **API:** Django REST Framework (DRF)  
- **Database:** SQLite (default)  
- **Admin Interface:** Django Admin  
- **Version Control:** Git & GitHub  

---

## 🗂️ Available API Endpoints (Read-Only)

| Method | Endpoint | Description |
|------|--------|------------|
| GET | `/books/` | List all books |
| GET | `/books/{id}/` | Retrieve a specific book |
| GET | `/authors/` | List all authors |
| GET | `/author/{id}/` | Retrieve Specific Author Information |
| GET | `/author/{id}/books/` | List all books by specific Author |
| GET | `/author/{id}/book/{id}/` | Retrive a specific book by a specific Author |

> ❗ POST, PUT, PATCH, DELETE are **disabled** for public users.

## 📑 API Documentation

Full API documentation is available in Notion:

[View API Documentation in Notion](https://www.notion.so/Bookshelf-Rest-API-Project-Documentation-2ebc3627c3d080e8b64fd3de57fb7ae9)

> This contains all endpoints, sample requests/responses, and usage instructions.

---