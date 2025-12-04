# FastAPI Backend Application

A minimal FastAPI backend application with a health check endpoint.

## Setup

### Option 1: Using uv (Recommended - Faster)

1. Create a virtual environment:
```bash
uv venv venv
```

2. Activate the virtual environment:
```bash
# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

### Option 2: Using pip

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server with auto-reload:
```bash
uvicorn app.main:app --reload
```

The application will be available at `http://localhost:8000`

## API Endpoints

- `GET /health` - Health check endpoint
  - Returns: `{"status": "healthy", "service": "fastapi-backend"}`

## API Documentation

FastAPI automatically generates interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing

Test the health check endpoint:
```bash
curl http://localhost:8000/health
```
