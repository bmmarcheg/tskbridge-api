from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class ProjectStatus(str, Enum):
    """Project status enumeration."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"


class ProjectSchema(BaseModel):
    """Project response schema."""
    id: str = Field(..., description="Project ID")
    name: str = Field(..., description="Project name")
    description: Optional[str] = None
    status: ProjectStatus = ProjectStatus.ACTIVE
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CreateProjectSchema(BaseModel):
    """Create project request schema."""
    name: str = Field(..., description="Project name")
    description: Optional[str] = None


class UpdateProjectSchema(BaseModel):
    """Update project request schema."""
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ProjectStatus] = None


class UpdateProjectStatusSchema(BaseModel):
    """Update project status request schema."""
    status: ProjectStatus = Field(..., description="New project status")
