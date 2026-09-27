# Campus Events Management System

A simple, robust Django + SQLite college project for managing campus events with complete CRUD operations.

## Technologies Used
- **Language:** Python 3.13
- **Framework:** Django 6.1
- **API:** Django REST Framework
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3, Bootstrap 5

## Key Features
- **Create:** Add new campus events with automatic validation
- **Read:** View all upcoming campus events and individual event details, with search functionality
- **Update:** Edit existing event details with pre-populated HTML5 datetime forms
- **Delete:** Remove events with a secure confirmation step
- **Admin Interface:** Django Admin panel for administrative control
- **REST API:** Fully functional REST endpoints for CRUD integration

## Main Application URLs
- **Home / Event List:** `http://127.0.0.1:8000/` or `http://127.0.0.1:8000/events/`
- **Add New Event:** `http://127.0.0.1:8000/events/add/`
- **REST API:** `http://127.0.0.1:8000/api/events/`
- **Django Admin:** `http://127.0.0.1:8000/admin/`

## How to Run the Project

1. Open PowerShell or Terminal in the project root folder:
   ```bash
   cd "C:\Users\Admin\Desktop\New folder (2)"
   ```

2. Run database migrations:
   ```bash
   .\venv\Scripts\python.exe manage.py migrate
   ```

3. (Optional) Create an Admin superuser:
   ```bash
   .\venv\Scripts\python.exe manage.py createsuperuser
   ```

4. Start the Django development server:
   ```bash
   .\venv\Scripts\python.exe manage.py runserver
   ```

5. Open your web browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## REST API Endpoints
- `GET /api/events/` - List all events
- `POST /api/events/` - Create a new event
- `GET /api/events/<id>/` - Retrieve an event by ID
- `PUT /api/events/<id>/` - Update an event
- `DELETE /api/events/<id>/` - Delete an event

## System Architecture
`User / Browser` &rarr; `Django URLs` &rarr; `Django Views / REST API` &rarr; `Django ModelForm / Serializer` &rarr; `SQLite Database`
