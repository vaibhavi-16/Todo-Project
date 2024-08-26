# Todo-Project

Project Overview
This project is a RESTful API built using Django that provides a simple and robust way to manage a todo list.The API supports full CRUD (Create, Read, Update, Delete) operations and is secured with JWT (JSON Web Token) authentication. It also integrates with a PostgreSQL database for efficient data management and uses Celery for asynchronous task processing.

**Features**

CRUD Operations: Easily create, read, update, and delete todo items.
Authentication: Secure API endpoints with JWT tokens.
Database Integration: Uses PostgreSQL for data storage with well-structured models and efficient queries.
Asynchronous Tasks: Processes background tasks using Celery.
Comprehensive Documentation: Includes setup instructions, API endpoint details, and deployment guidelines.

**Setup Instructions**
Python 3.x
PostgreSQL
Redis (for Celery)
Git

**Installation Clone the repository:**
git clone https://github.com/your-username/Todo-Project.git
cd Todo-Project

**Set up a virtual environment and activate it:**
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the dependencies:
pip install -r requirements.txt

**Configure the database:**
Update the DATABASES settings in settings.py to match your PostgreSQL configuration.
**Apply database migrations:**
python manage.py makemigrations
python manage.py migrate

**Run the development server:**
python manage.py runserver
Running the Code Locally
Start the Celery worker:
celery -A todo_project worker --loglevel=info

**Run the Django server:**
python manage.py runserver

**Access the API locally:**
Navigate to http://127.0.0.1:8000/api/ in your browser or use a tool like Postman.

**API Endpoints Documentation**
GET /api/todos/: Retrieve a list of all todo items.

POST /api/todos/: Create a new todo item.

GET /api/todos/{id}/: Retrieve a specific todo item by ID.

PUT /api/todos/{id}/: Update a specific todo item by ID.

DELETE /api/todos/{id}/: Delete a specific todo item by ID.

POST /api/token/: Obtain JWT token for authentication.

POST /api/token/refresh/: Refresh JWT token.
