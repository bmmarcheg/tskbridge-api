# Copilot Instructions for TaskBridge API

## Technology Stack

This project uses:
- **Language**: Python 3.9+
- **Framework**: FastAPI
- **Package Manager**: pip
- **Testing**: pytest

## Code Style and Conventions

### Python Standards
- Follow PEP 8 style guidelines
- Use type hints for all function parameters and return types
- Use docstrings for all functions, classes, and modules (Google style)
- Maximum line length: 100 characters

### FastAPI Conventions
- Define routes using path operations (`@app.get()`, `@app.post()`, etc.)
- Use Pydantic models for request/response schemas
- Always include proper HTTP status codes and error handling
- Use dependency injection for shared logic
- Document endpoints with docstrings and OpenAPI annotations

### Project Structure
```
src/
├── projects/          # Projects service
│   ├── models.py      # Pydantic models and data structures
│   ├── service.py     # Business logic
│   ├── routes.py      # API endpoints
│   └── schemas.py     # Request/response schemas
├── notifications/     # Notifications service
│   ├── models.py
│   ├── service.py
│   ├── routes.py
│   └── schemas.py
├── core/
│   ├── config.py      # Configuration management
│   └── dependencies.py # Shared dependencies
└── main.py            # Application entry point
```

## Example Patterns

### FastAPI Route with Type Hints
```python
from fastapi import APIRouter, HTTPException, status
from typing import List

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("/", response_model=List[ProjectSchema])
async def list_projects() -> List[ProjectSchema]:
    """Retrieve all projects."""
    return await project_service.get_all_projects()

@router.post("/", response_model=ProjectSchema, status_code=status.HTTP_201_CREATED)
async def create_project(project: CreateProjectSchema) -> ProjectSchema:
    """Create a new project."""
    return await project_service.create(project)
```

### Pydantic Model Example
```python
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProjectSchema(BaseModel):
    """Project response schema."""
    id: str = Field(..., description="Project ID")
    name: str = Field(..., description="Project name")
    description: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True
```

### Service Layer Example
```python
class ProjectService:
    """Service for project operations."""
    
    async def get_all_projects(self) -> list[dict]:
        """Retrieve all projects from database."""
        # Implementation here
        pass
    
    async def create(self, project_data: CreateProjectSchema) -> dict:
        """Create a new project."""
        # Implementation here
        pass
```

## Testing Guidelines

- Write tests using pytest
- Use fixtures for setup and teardown
- Test files should mirror the source structure: `tests/test_projects/`
- Aim for high coverage on business logic

Example test:
```python
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def sample_project():
    return {"name": "Test Project", "description": "A test project"}

def test_create_project(sample_project):
    response = client.post("/projects/", json=sample_project)
    assert response.status_code == 201
    assert response.json()["name"] == sample_project["name"]
```

## Error Handling

- Use FastAPI's HTTPException for API errors
- Always provide meaningful error messages
- Use appropriate HTTP status codes
- Include error details in responses

```python
from fastapi import HTTPException, status

if not project:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Project not found"
    )
```

## Dependencies and Requirements

When suggesting packages:
- FastAPI: Web framework
- Uvicorn: ASGI server
- Pydantic: Data validation
- SQLAlchemy: ORM (if database needed)
- pytest: Testing framework
- python-dotenv: Environment variables

## Additional Notes

- Use async/await for all I/O operations
- Implement proper logging throughout the application
- Keep services focused on single responsibilities
- Use environment variables for configuration
