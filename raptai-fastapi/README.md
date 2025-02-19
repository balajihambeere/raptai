# raptai-fastapi

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