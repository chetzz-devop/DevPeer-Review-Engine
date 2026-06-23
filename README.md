DevPeer API
DevPeer API is a production-grade, secure RESTful backend engine designed for a developer portfolio and peer-evaluation network. It allows software engineers to create profiles, showcase their projects with validated links, and receive authenticated, structured peer reviews and star ratings.

🚀 Core Features
Secure Authentication: Integrated SimpleJWT (JSON Web Tokens) to secure endpoints and manage user sessions.

Dual-Layer Data Integrity: Built-in validators at both the Serializer and Database levels to ensure rigorous input validation.

Anti-Gaming Logic: Custom object-level validation preventing users from reviewing or rating their own projects.

Optimized Database Queries: Modeled relational database architectures utilizing Django ORM reverse lookups (related_name) to minimize query overhead.

Advanced Query Performance: Support for text search, multi-field filtering, and custom ordering parameters out of the box.

🛠️ Tech Stack
Framework: Django 6.0 & Django REST Framework (DRF)

Authentication: JWT (Django REST Framework SimpleJWT)

Database: SQLite3 (Development) / Production-ready for PostgreSQL

Language: Python 3.14+

📂 Database Architecture
The API uses a highly structured relational schema to maintain strict data consistency:

User ↔ Profile: OneToOneField mapping ensures every registered user has exactly one developer profile.

Profile ↔ Project: One-to-Many (ForeignKey) relationship mapping a developer to their portfolio submissions.

Profile/Project ↔ Review: Many-to-One relationships utilizing optimized reverse lookup routing (related_name="reviews").

🛣️ API Endpoints
Method	Endpoint	Description	Auth Required
POST	/api/token/	Obtain JWT Access & Refresh Tokens	No
POST	/api/token/refresh/	Refresh expired JWT Access Token	No
GET	/dev/	List all developer projects (Supports search/filter)	No
POST	/dev/	Submit a new project portfolio	Yes
GET	/reviews/	View all submitted project reviews and ratings	No
POST	/reviews/	Submit a star rating and comment on a project	Yes
🔒 Crucial Business Logic & Rules
1. Project Link Formatting
The project_link field uses a strict URLValidator. Input addresses must include the absolute protocol scheme (e.g., https://).

❌ Invalid: www.github.com/username

✅ Valid: https://www.github.com/username

2. Peer Review Constraints
The ReviewSerializer evaluates the incoming payload against two key production rules before performing database transactions:

The star rating value must be an integer between 1 and 5.

The author profile ID cannot match the project owner profile ID. Attempting to rate your own work returns a 400 Bad Request with an explicit security validation error.
#Screen Shots of how project looks like 

<img width="1915" height="952" alt="Screenshot 2026-06-23 175307" src="https://github.com/user-attachments/assets/255e0ea2-b45b-4c27-8790-88c9c0cba673" />
<img width="1918" height="983" alt="Screenshot 2026-06-23 175318" src="https://github.com/user-attachments/assets/f65ba017-fe6f-46e3-9801-9adf65df9911" />
<img width="1918" height="987" alt="Screenshot 2026-06-23 175356" src="https://github.com/user-attachments/assets/56bb8b41-466b-42a9-b1c9-0dee48cc99ee" />





⚙️ Setup & Installation
Clone the repository:

Bash
git clone https://github.com/yourusername/devpeer-api.git
cd devpeer-api
Set up a virtual environment and install dependencies:

Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

pip install django djangorestframework djangorestframework-simplejwt django-filter
Run database migrations:

Bash
python manage.py makemigrations
python manage.py migrate
Start the local development server:

Bash
python manage.py runserver
The API will be locally accessible at http://127.0.0.1:8000/.
