# 🚨 Emergency Service Portal

A web-based Emergency Service Portal developed to provide citizens with quick access to emergency resources, volunteer support, healthcare information, and lost & found services through a centralized platform.

The system enables both users and administrators to manage emergency-related information efficiently using a secure, database-driven architecture built with PHP and MySQL.

---

## 📖 Project Overview

The Emergency Service Portal was developed as part of the **CSE370: Database Systems** course at **BRAC University**.

The platform aims to simplify access to emergency services by integrating multiple community support modules into a single application, including:

- 🚑 Healthcare Information
- 🚨 SOS Services
- ❤️ Volunteer Management
- 🔍 Lost & Found System
- 👨‍💼 Administrative Dashboard

The system provides separate interfaces for users and administrators while ensuring secure database interactions using prepared SQL statements.

---

# ✨ Features

## 👤 User Features

### User Registration

- Register with personal information
- Store user details securely in the database

### Healthcare Services

- Search healthcare information using User ID
- View hospital contacts
- View doctor information
- Access telemedicine availability

### SOS Services

- Search emergency contacts by:
  - Area
  - User ID

Available services include:

- Police
- Fire Service
- Women's Helpline

### Volunteer Services

- Register as a volunteer
- Search volunteers by blood group
- View volunteer information

### Lost & Found

- Report lost items
- View recently reported items
- Search available records

---

## 🔐 Admin Features

### Dashboard

Centralized admin dashboard for managing all services.

### Healthcare Management

- Add healthcare information
- View healthcare records
- Delete healthcare records

### SOS Management

- Add SOS information
- View SOS records
- Delete SOS records

### Volunteer Management

- View volunteer registrations
- Delete volunteer records
- Search volunteers

### Lost & Found Management

- View reported items
- Delete recovered items

---

# 🗄 Database Design

The application is powered by a relational MySQL database consisting of:

- User
- Healthcare
- Volunteer
- SOS
- Lost and Found

The database maintains relationships between users and emergency-related information for efficient retrieval and management.

---

# 🏗 System Architecture

```
User
      │
      ▼
HTML / CSS Frontend
      │
      ▼
PHP Backend
      │
      ▼
MySQL Database
```

---

# 💻 Tech Stack

## Frontend

- HTML5
- CSS3

## Backend

- PHP

## Database

- MySQL

## Development Concepts

- CRUD Operations
- Relational Database Design
- Session Authentication
- Prepared Statements
- Input Validation

---

# 🔒 Security Features

The system implements several security measures:

- Prepared SQL Statements
- SQL Injection Prevention
- Session-based Authentication
- Input Validation
- Secure CRUD Operations

---

# 📂 Project Modules

```
Emergency-Service-Portal

├── User Module
│   ├── Registration
│   ├── Dashboard
│   └── Navigation
│
├── Healthcare Module
│   ├── Search Healthcare
│   ├── Add Healthcare
│   ├── View Healthcare
│   └── Delete Healthcare
│
├── SOS Module
│   ├── Search SOS
│   ├── Add SOS
│   ├── View SOS
│   └── Delete SOS
│
├── Volunteer Module
│   ├── Registration
│   ├── Search by Blood Group
│   ├── View Volunteers
│   └── Delete Volunteers
│
├── Lost & Found Module
│   ├── Report Item
│   ├── View Items
│   └── Delete Item
│
└── Admin Dashboard
```

---

# 📸 Screenshots

Screenshots can be added here.

Example:

```
screenshots/
│
├── homepage.png
├── dashboard.png
├── healthcare.png
├── volunteer.png
├── sos.png
└── admin.png
```

---

# 👥 Team Contributions

### Aisha Islam

Healthcare Module

Frontend

- Designed Healthcare Admin interface
- Developed Healthcare Search page
- Created responsive UI for healthcare services

Backend

- Implemented healthcare search using PHP & MySQL
- Developed admin healthcare management
- Implemented secure database retrieval using prepared statements
- Developed delete functionality for healthcare records

---

### Tasbir Ahmed

- Lost & Found Module
- Volunteer Module

---

### Ahnaf Jahin

- SOS Module
- Volunteer Backend
- Authentication

---

# 🎯 Learning Outcomes

This project provided practical experience in:

- Database Design
- SQL
- PHP Backend Development
- CRUD Operations
- Session Management
- Responsive Web Design
- Client–Server Architecture
- Team Collaboration
- Software Documentation

---

# 🚀 Future Improvements

Possible future enhancements include:

- Responsive mobile interface
- Google Maps integration
- SMS & Email notifications
- Live emergency tracking
- Role-based authentication
- JWT Authentication
- REST API integration
- Cloud deployment
- Digital medical records
- AI-powered emergency assistance

---

# 📚 Course Information

**Course:** CSE370 – Database Systems

**Institution:** BRAC University

---

# 📄 Documentation

The complete project report, including:

- System Design
- ER Diagram
- Database Schema
- Frontend Design
- Backend Implementation
- Module Documentation

is included in the repository.

---

# ⚠️ Note

This repository is maintained for academic and portfolio purposes.

The original source code is currently unavailable. The repository contains comprehensive project documentation describing the complete system architecture, implementation, database design, and individual team contributions.

---

# 📜 License

This project is intended for educational purposes only.
