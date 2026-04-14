# 🚀 TeamFlow Backend (FastAPI)

A production-style backend for a team collaboration and project management tool (like Trello/Jira).

---

## 🧠 Features Implemented (Day 1)

### 🔐 Authentication System

* JWT-based authentication
* Secure password hashing (bcrypt + SHA256 pre-hash)
* Login & Register APIs
* Protected routes using OAuth2

---

### 👤 User System

* Unified user model (supports OAuth + local auth)
* UUID-based IDs
* Scalable schema design

---

### 🏢 Workspace & Roles

* Multi-tenant architecture
* Workspace creation
* Role-based system (owner, admin, member)

---

### 📁 Projects & Tasks

* Projects inside workspaces
* Tasks with:

  * status (Kanban-ready)
  * priority
  * assignment
  * drag-drop support (position field)

---

### 💬 Collaboration Features

* Task comments
* Activity logging system (with JSON details)

---

### 🧱 Backend Architecture

* Clean folder structure:

  * `models/`
  * `schemas/`
  * `services/`
  * `api/`
* Separation of concerns

---

## ⚙️ Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* JWT (python-jose)
* Passlib (bcrypt)

---

## 🚀 How to Run

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## 🔥 Upcoming Features

* OTP Email Verification
* Password Reset
* OAuth (Google + GitHub)
* Redis Caching
* Notifications System

---

## 🧠 Learning Highlights

* Designed a scalable multi-tenant backend
* Implemented secure authentication flows
* Built role-based authorization system
* Structured codebase like production systems
