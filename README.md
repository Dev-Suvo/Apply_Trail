# ApplyTrail

Smart job application tracker built with Django REST Framework.

## Tech Stack
- Python 3.11+, Django, Django REST Framework
- PostgreSQL
- JWT Auth (djangorestframework-simplejwt)
- django-filter, Celery + Redis, Docker

## API Endpoints (planned)

| Method | Endpoint                  | Description                        | Status      |
|--------|----------------------------|-------------------------------------|-------------|
| POST   | /api/register/             | Register a new user                 | Not started |
| POST   | /api/token/                 | Login (get JWT access/refresh)     | Not started |
| POST   | /api/token/refresh/        | Refresh JWT token                   | Not started |
| GET    | /api/applications/         | List logged-in user's applications | Not started |
| POST   | /api/applications/         | Create a new application            | Not started |
| GET    | /api/applications/{id}/    | Retrieve one application            | Not started |
| PUT    | /api/applications/{id}/    | Update an application                | Not started |
| DELETE | /api/applications/{id}/    | Delete an application                | Not started |
| GET    | /api/tags/                 | List tags                           | Not started |
| GET    | /api/dashboard/             | Application stats summary           | Not started |