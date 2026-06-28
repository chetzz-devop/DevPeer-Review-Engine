# Developer API

A Django REST Framework backend for managing developer portfolio projects and peer reviews.

## Project Overview

Developer API enables registered users to create, update, delete, and list developer projects, while allowing authenticated users to submit peer reviews and ratings. The system enforces owner-only edit/delete permissions and prevents users from reviewing their own projects.

## Technology Stack

- Python 3
- Django 6.0.6
- Django REST Framework
- djangorestframework-simplejwt
- django-filter
- SQLite3
- JWT authentication + Session authentication

## Core Features

- Full CRUD operations for `Project` objects
- Peer review submission with rating limits (1-5 stars)
- JWT access and refresh token authentication
- Session authentication fallback
- Owner-only modification via custom permission class
- Project URL validation on submission
- Filtering by project title and ordering support
- Global pagination with 5 items per page
- Admin registration for Project, Profile, and Review models

## Data Models

- `Profile` — extends Django `User` with bio information
- `Project` — stores project owner, title, and project link
- `Review` — stores review author, project, comment, and rating value

## API Endpoints

- `POST /api/token/` — obtain JWT access and refresh tokens
- `POST /api/token/refresh/` — refresh an access token
- `GET /dev/` — list projects
- `POST /dev/` — create a new project
- `GET /dev/<id>/` — retrieve project details
- `PUT /dev/<id>/` — update a project (owner only)
- `DELETE /dev/<id>/` — delete a project (owner only)
- `POST /dev/review/` — submit a review for a project
### Screen Shots 
<img width="1915" height="952" alt="Screenshot 2026-06-23 175307" src="https://github.com/user-attachments/assets/f51a45d4-51f1-4b14-9e91-a183728c776d" />
<img width="1918" height="987" alt="Screenshot 2026-06-23 175356" src="https://github.com/user-attachments/assets/a88d493b-0a6c-47e3-925f-fd7d3fc81534" />

## Setup

1. Open a terminal in the project root.
2. Activate the Python virtual environment if available:
   - Windows PowerShell: `& ".venv\Scripts\Activate.ps1"`
3. Install dependencies:
   - `pip install django djangorestframework djangorestframework-simplejwt django-filter`
4. Navigate to the Django project directory:
   - `cd dev`
5. Apply migrations:
   - `python manage.py migrate`
6. Create a superuser for admin access (optional):
   - `python manage.py createsuperuser`
7. Run the development server:
   - `python manage.py runserver`

## Usage Notes

- The app currently uses SQLite3 as the database.
- The API root is served from the top-level URL via `devapp.urls`.
- Use the admin site at `/admin/` to inspect `Profile`, `Project`, and `Review` records.

## Skills Demonstrated

- Django REST Framework API design
- JWT authentication and refresh token flows
- Custom permission classes and object-level authorization
- Serializer validation and business rule enforcement
- Model relationships with Django ORM
- Filtering, ordering, and pagination
- Secure API patterns and Django middleware

## HR-Focused Summary

Built a production-oriented backend API for developer portfolio management with strong authentication, authorization, and validation practices. Demonstrated practical experience in Django, REST API architecture, and secure token-based access control.

## Resume-Ready Bullets

- Developed a Django REST Framework API for project portfolio management and peer reviews using JWT authentication, custom authorization, and validation rules.
- Implemented owner-only project editing, review rating enforcement, and project URL validation.
- Added filtering, ordering, and paginated API responses for scalable data retrieval.
- Modeled relational data in Django ORM and registered core models in the admin interface.
