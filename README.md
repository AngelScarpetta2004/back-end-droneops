#  DroneOps Back-End (Python/Django)

**DroneOps** is a backend API designed to manage drone operations, including **telemetry data** logging, repairs, events, and inventory.
This project provides a scalable and modular foundation for drone management systems using the **Django framework** and **Django REST Framework** for API construction.

---

##  Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Project Structure](#project-structure)
5. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Database Setup](#database-setup)
   - [Running the Server](#running-the-server)
6. [API Endpoints](#api-endpoints)
7. [Data Models](#data-models)
8. [Authentication](#authentication)
9. [Testing](#testing)
10. [Contributing](#contributing)
11. [License](#license)
12. [Contact](#contact)

---

## Overview

The **DroneOps Back-End** manages core drone operations, focusing on the **structuring and validation of critical data** such as telemetry records, repair history, inventory control, and user authentication.
It provides a RESTful API that can be easily connected to any front-end or mobile application for comprehensive management.

---

## Features

- **User Authentication and Authorization**
  Registration, login, and token-based authentication (JWT) implemented using **Django REST Framework SimpleJWT**.

- **Drone Management**
  CRUD operations for drones, with built-in data validation for model, serial number, and operational status.

- **Telemetry and Events**
  **Logging, structuring, and monitoring of large volumes of telemetry data** (events and alerts), using Django models to ensure relational integrity.

- **Repairs and Maintenance**
  **Tracking of maintenance data**, parts replaced, actions taken, and history within a relational schema.

- **Inventory Control**
  Management of spare parts and components inventory, leveraging the Django ORM for secure stock transactions.

- **Scalable Architecture**
  Modular structure based on Django's MVT (Model-View-Template) pattern.

- **Validation and Error Handling**
  **Centralized input data validation** via Django Serializers to ensure data quality and consistency.

---

## Tech Stack

| Category | Technology |
| :--- | :--- |
| Runtime Environment | **Python** |
| Framework | **Django** (with Django REST Framework) |
| Database | **MySQL/PostgreSQL** (Using Django ORM) |
| Authentication | **Django REST Framework SimpleJWT** |
| Validation | **Django Serializers / Argon2** |
| Version Control | **Git & GitHub** |

---

## Project Structure

back-end-droneops/
│
├── droneops_project/ # Main configuration directory
│   ├── settings.py # Database and app configuration
│   └── urls.py # Main project routes
│
├── **apps/** # Application modules
│   ├── **drones/** # Models, Views, and Serializers for Drones and Telemetry
│   ├── **repairs/** # Models, Views, and Serializers for Repair Records
│   └── **inventory/** # Models, Views, and Serializers for Inventory Control
│
├── **manage.py** # Django command-line utility
└── **requirements.txt** # Python dependencies

---

## Getting Started

### Prerequisites

Before running the project, make sure you have the following installed:

- **Python** (v3.x recommended)
- **pip**
- A **PostgreSQL or MySQL** instance (for production)
- **Git**

### Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/AngelScarpetta2004/back-end-droneops.git](https://github.com/AngelScarpetta2004/back-end-droneops.git)
   cd back-end-droneops

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

### Running the Server

   To start the Django development server:
    ```bash
      
      python manage.py runserver
 
 The server will be available at http://127.0.0.1:8000/

 ## API Endpoints

All endpoints are prefixed with `/api/`.

### Authentication

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | `/api/auth/register` | Register a new user |
| POST | `/api/auth/login` | Log in and get JWT token |
| POST | `/api/auth/token/refresh` | Refresh access token |

---

### Drones

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | `/api/drones` | Get all drones |
| POST | `/api/drones` | Create a new drone record |
| GET | `/api/drones/:id` | Get drone by ID |
| PUT/PATCH | `/api/drones/:id` | Update drone information |
| DELETE | `/api/drones/:id` | Delete drone record |

---

### Repairs

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | `/api/repairs` | List all repair records |
| POST | `/api/repairs` | Add a new repair record |
| GET | `/api/repairs/:id` | Get repair details |

---

### Events & Telemetry

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | `/api/events` | Get all events and telemetry data |
| POST | `/api/events` | Log a new drone event (telemetry data) |

---

### Inventory

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | `/api/inventory` | View parts and stock |
| POST | `/api/inventory` | Add new part or stock item |

---

## Data Models (Django ORM Structure Example)

Models are defined using the Django ORM.

### User

      ```json

         {
            "username": "String",
            "email": "String",
            "password": "String (hashed with Argon2)",
            "role": "String (admin, operator)"
         }

### Drone

      ```json
      {
        "id": "AutoField (Primary Key)",
        "model": "String",
        "serialNumber": "String",
        "status": "String",
        "purchaseDate": "DateField"
      }
### Repair

       ```json
      {
        "id": "AutoField (Primary Key)",
        "droneId": "ForeignKey to Drone",
        "description": "String",
        "dateReported": "DateTimeField",
        "dateResolved": "DateTimeField",
        "cost": "DecimalField",
        "partsUsed": "TextField or JSONField"
      }

### Event

       ```json
      {
        "id": "AutoField (Primary Key)",
        "droneId": "ForeignKey to Drone",
        "eventType": "String",
        "timestamp": "DateTimeField",
        "description": "String"
      }
      
### Authentication

JWT-based authentication (via DRF SimpleJWT)
Tokens are issued upon login and must be included in the request headers to access protected routes:

Authorization: Bearer <token>

###Testing

If you have tests configured, run them with the native Django command:

      ```bash
         python manage.py test

### Contributing

Contributions, bug reports, and feature requests are welcome!

1. Fork the project

2. Create a new branch: `git checkout -b feature/new-feature`

3. Commit your changes: `git commit -m "Add new feature"`

4. Push to the branch: `git push origin feature/new-feature`

5. Submit a pull request

### License

This project is licensed under the MIT License.
© 2025 Angel Scarpetta

### Contact

Author: Angel Scarpetta
GitHub: @AngelScarpetta2004
Repository: DroneOps Back-End

### Summary

DroneOps Back-End provides a reliable and scalable foundation for managing drone operations, excelling in the structuring and handling of critical data — from telemetry and events to maintenance tracking to inventory control. It is designed for optimal performance and easy integration with any application.
    
