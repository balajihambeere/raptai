# raptai-fastapi

![fastapi-book-cover](https://github.com/user-attachments/assets/8e9a87ae-e953-4cae-a640-e128de6ccfae)

## Using poetry
```bash
 poetry install
```
## Using virtual environment
```bash
 pip install -r requirements.tsx
```

##
```bash
# Run application
cd src
cd app

# run following command
uvicorn main:app --host 0.0.0.0 --port 80
 
```
## Add to .env
```bash
PROJECT_NAME=<> # Project name
DATABASE_URL=<> # Database URL
DB_FORCE_ROLL_BACK=False
SECRET_KEY = <> # Secret key
ALGORITHM = HS256
ACCESS_TOKEN_EXPIRE_MINUTES = 30
```

## Project Architecture Architecture

```bash
raptai-fastapi/
├── src/
|   ├──app 
│   |   ├── __init__.py
│   |   ├── main.py                  # FastAPI app entry point
│   ├── core/                    # Core application logic
│   │   ├── __init__.py
│   │   ├── config.py            # Configuration settings (e.g., environment variables)
│   │   ├── security.py          # Authentication and authorization logic
│   │   ├── exceptions.py        # Custom exceptions
│   │   └── logging.py           # Logging configuration
│   ├── api/                     # API endpoints (routers)
│   │   ├── __init__.py
│   │   ├── v1/                  # Versioned API endpoints
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/       # Endpoints grouped by functionality
│   │   │   │   ├── users.py
│   │   │   │   ├── products.py
│   │   │   │   └── ...
│   │   │   └── routers.py       # Aggregates all routers for v1
│   │   └── v2/                  # Future API version
│   ├── models/                  # Database models (SQLAlchemy, Pydantic, etc.)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── product.py
│   │   └── ...
│   ├── schemas/                 # Pydantic schemas for request/response validation
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── product.py
│   │   └── ...
│   ├── services/                # Business logic and service layer
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   ├── product_service.py
│   │   └── ...
│   ├── repositories/            # Database interaction layer
│   │   ├── __init__.py
│   │   ├── user_repository.py
│   │   ├── product_repository.py
│   │   └── ...
│   ├── dependencies/            # Dependency injection logic
│   │   ├── __init__.py
│   │   ├── auth.py              # Auth dependencies
│   │   └── database.py          # Database session dependencies
│   ├── utils/                   # Utility functions and helpers
│   │   ├── __init__.py
│   │   ├── email.py
│   │   ├── validation.py
│   │   └── ...
│   ├── tests/                   # Unit and integration tests
│   │   ├── __init__.py
│   │   ├── unit/
│   │   │   ├── test_users.py
│   │   │   ├── test_products.py
│   │   │   └── ...
│   │   └── integration/
│   │       ├── test_api.py
│   │       └── ...
│   └── migrations/              # Database migrations (e.g., Alembic)
│       ├── versions/
│       ├── env.py
│       └── alembic.ini
├── requirements.txt             # Project dependencies
├── requirements-dev.txt         # Development dependencies
├── .env                         # Environment variables
├── .gitignore                   # Git ignore file
├── Dockerfile                   # Docker configuration
├── docker-compose.yml           # Docker Compose configuration
└── README.md                    # Project documentation
```


A few important notes about these configurations:

### The Dockerfile:

- Uses Python 3.9 slim image to keep the container size small

- Copies requirements first to leverage Docker layer caching

- Sets environment variables

- Exposes port 8000 (adjust if your application uses a different port)

### The docker-compose.yml:

- Defines two services: web (your application) and db (PostgreSQL)

- Sets up environment variables for both services

- Creates a persistent volume for PostgreSQL data

- Sets up proper networking between containers

- Maps ports to host machine

- Uses depends_on to ensure database starts before the web application

### Security considerations:

- In a production environment, you should not include sensitive information like SECRET_KEY in the Dockerfile or docker-compose.yml

- Consider using Docker secrets or environment files for sensitive information

- The PostgreSQL password should be more secure in production

### To run the application:

1. Make sure Docker and Docker Compose are installed

2. Place these files in your project root

3. Run `docker-compose up --build`

This will build the images and start the containers. Your application should be accessible at http://localhost:8000.