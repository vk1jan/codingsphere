# FastAPI JWT Authentication with RBAC

This project implements a RESTful API with JWT authentication and Role-Based Access Control (RBAC) using FastAPI and PostgreSQL with SQLModel as the ORM.

## Features

- User registration and login
- Secure password hashing using bcrypt
- JWT token authentication
- Role-based access control (admin and user roles)
- CRUD operations for projects with role-based permissions
- PostgreSQL database with SQLModel ORM

## Prerequisites

- Python 3.9+
- PostgreSQL

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/fastapi-jwt-rbac.git
cd fastapi-jwt-rbac
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the PostgreSQL database:

Make sure PostgreSQL is running and create a database named `jwt_rbac_db`.

Update the database connection string in `app/database.py` if needed:

```python
DATABASE_URL = "postgresql://postgres:password@localhost:5432/jwt_rbac_db"
```

## Running the Application

Start the application:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

Interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Authentication

- `POST /register` - Register a new user
- `POST /login` - Log in and get an access token

### Projects

- `GET /projects` - Get all projects (user and admin)
- `GET /projects/{project_id}` - Get a specific project (user and admin)
- `POST /projects` - Create a new project (admin only)
- `PUT /projects/{project_id}` - Update a project (admin only)
- `DELETE /projects/{project_id}` - Delete a project (admin only)

### User Info

- `GET /me` - Get current user information

## Usage Examples

### Register a User

```bash
curl -X 'POST' \
  'http://localhost:8000/register' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "password123",
  "role": "user"
}'
```

### Login and Get Token

```bash
curl -X 'POST' \
  'http://localhost:8000/login' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=john_doe&password=password123'
```

### Create a Project (Admin Only)

```bash
curl -X 'POST' \
  'http://localhost:8000/projects' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Project A",
  "description": "Description of project"
}'
```

### Get All Projects

```bash
curl -X 'GET' \
  'http://localhost:8000/projects' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN'
```

## Security Notes

- For a production environment, store the JWT secret key securely (e.g., using environment variables)
- Configure CORS settings appropriately for your deployment
- Consider adding more comprehensive error handling and validation