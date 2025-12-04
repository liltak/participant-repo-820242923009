# Design Document

## Overview

This design outlines the structure and components for a dual-component project consisting of a FastAPI Python backend and an AWS CDK infrastructure project. The design focuses on creating a clean, organized foundation that follows best practices for both FastAPI applications and CDK projects.

## Architecture

The project follows a monorepo structure with two independent but related components:

```
project-root/
├── .git/
├── .gitignore
├── README.md
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   └── main.py
│   ├── requirements.txt
│   └── README.md
└── infrastructure/
    ├── app.py
    ├── infrastructure/
    │   ├── __init__.py
    │   └── infrastructure_stack.py
    ├── requirements.txt
    ├── cdk.json
    └── README.md
```

### Design Decisions

1. **Monorepo Structure**: Both components live in the same repository to simplify version control and coordination between backend and infrastructure changes
2. **Separate Dependencies**: Each component maintains its own requirements.txt to allow independent dependency management
3. **Standard Naming**: Using conventional directory names (backend/, infrastructure/) for clarity
4. **Minimal Scaffolding**: Focus on essential files only, avoiding over-engineering

## Components and Interfaces

### Backend Application Component

**Purpose**: Provides a FastAPI web application scaffold with minimal setup

**Key Files**:
- `backend/app/main.py`: Main FastAPI application with health check endpoint
- `backend/requirements.txt`: Python dependencies (fastapi, uvicorn)
- `backend/README.md`: Documentation for running the backend

**API Interface**:
- `GET /health`: Health check endpoint returning status information

### CDK Infrastructure Component

**Purpose**: Provides AWS CDK project structure for defining cloud resources

**Key Files**:
- `infrastructure/app.py`: CDK app entry point
- `infrastructure/infrastructure/infrastructure_stack.py`: Main CDK stack definition
- `infrastructure/requirements.txt`: CDK dependencies
- `infrastructure/cdk.json`: CDK configuration
- `infrastructure/README.md`: Documentation for deploying infrastructure

**Stack Interface**:
- Empty stack ready for resource definitions

## Data Models

### Backend Health Check Response
```python
{
    "status": "healthy",
    "service": "fastapi-backend"
}
```

### CDK Stack
- Basic CDK Stack class with no resources initially
- Extensible for adding AWS resources

## Error Handling

### Backend Application
- FastAPI's built-in exception handling for HTTP errors
- Uvicorn handles server-level errors

### CDK Infrastructure
- CDK CLI handles synthesis and deployment errors
- Stack validation occurs during synthesis

## Testing Strategy

### Backend Application
- Manual testing: Start server and curl the health endpoint
- Future: Unit tests for endpoints using FastAPI TestClient

### CDK Infrastructure
- CDK synthesis validation: `cdk synth` to verify stack can be synthesized
- Future: CDK assertions for testing infrastructure constructs

## Development Workflow

### Backend Development
1. Create virtual environment: `python -m venv venv`
2. Activate virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run application: `uvicorn app.main:app --reload`
5. Test endpoint: `curl http://localhost:8000/health`

### Infrastructure Development
1. Create virtual environment: `python -m venv venv`
2. Activate virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Bootstrap CDK (first time): `cdk bootstrap`
5. Synthesize stack: `cdk synth`
6. Deploy stack: `cdk deploy`

## Configuration

### Backend Configuration
- Default port: 8000
- Host: 0.0.0.0 (configurable via uvicorn CLI)
- Reload mode enabled for development

### CDK Configuration
- App: `python app.py`
- Language: Python
- CDK version: Latest stable (2.x)

## Dependencies

### Backend Dependencies
```
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
```

### Infrastructure Dependencies
```
aws-cdk-lib>=2.100.0
constructs>=10.0.0
```

## Git Configuration

### .gitignore Patterns
- Python: `__pycache__/`, `*.py[cod]`, `venv/`, `.env`
- CDK: `cdk.out/`, `.cdk.staging/`
- IDE: `.vscode/`, `.idea/`, `*.swp`
- OS: `.DS_Store`, `Thumbs.db`
