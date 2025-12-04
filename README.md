# FastAPI + AWS CDK Project

This project contains a FastAPI Python backend application and an AWS CDK infrastructure project for deploying cloud resources.

## Project Structure

```
.
├── backend/              # FastAPI backend application
│   ├── app/             # Application code
│   ├── requirements.txt # Python dependencies
│   └── README.md        # Backend setup instructions
│
└── infrastructure/       # AWS CDK infrastructure project
    ├── infrastructure/  # CDK stack definitions
    ├── app.py          # CDK app entry point
    ├── requirements.txt # CDK dependencies
    ├── cdk.json        # CDK configuration
    └── README.md       # Infrastructure deployment instructions
```

## Components

### Backend Application
A FastAPI-based web application providing REST API endpoints. See `backend/README.md` for setup and usage instructions.

### Infrastructure
AWS CDK project for defining and deploying cloud infrastructure as code. See `infrastructure/README.md` for deployment instructions.

## Getting Started

Each component has its own README with detailed setup instructions:
- Backend: `backend/README.md`
- Infrastructure: `infrastructure/README.md`

## Development

Both components use Python virtual environments for dependency isolation. Create and activate a virtual environment in each directory before installing dependencies.
