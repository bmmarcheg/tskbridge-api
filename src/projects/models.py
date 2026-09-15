from datetime import datetime
from typing import Optional
from enum import Enum


class ProjectStatus(str, Enum):
    """Project status enumeration."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"


class Project:
    """Project data model."""

    def __init__(
        self,
        id: str,
        name: str,
        description: Optional[str] = None,
        status: ProjectStatus = ProjectStatus.ACTIVE,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        """Initialize a project.
        
        Args:
            id: Project ID.
            name: Project name.
            description: Project description.
            status: Project status.
            created_at: Creation timestamp.
            updated_at: Last update timestamp.
        """
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def to_dict(self) -> dict:
        """Convert project to dictionary.
        
        Returns:
            Project as dictionary.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
