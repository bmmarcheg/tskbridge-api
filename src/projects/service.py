from datetime import datetime
from typing import Optional, Dict, List
import uuid
from .schemas import ProjectSchema, CreateProjectSchema, UpdateProjectSchema, ProjectStatus


class ProjectService:
    """Service for project operations."""

    def __init__(self):
        """Initialize project service with in-memory storage."""
        self.projects: Dict[str, Dict] = {}

    async def create(self, project_data: CreateProjectSchema) -> ProjectSchema:
        """Create a new project.
        
        Args:
            project_data: Project creation data.
            
        Returns:
            Created project schema.
        """
        project_id = str(uuid.uuid4())
        now = datetime.utcnow()
        
        project = {
            "id": project_id,
            "name": project_data.name,
            "description": project_data.description,
            "status": ProjectStatus.ACTIVE,
            "created_at": now,
            "updated_at": now,
        }
        
        self.projects[project_id] = project
        return ProjectSchema(**project)

    async def get(self, project_id: str) -> Optional[ProjectSchema]:
        """Retrieve a project by ID.
        
        Args:
            project_id: Project ID.
            
        Returns:
            Project schema or None if not found.
        """
        project = self.projects.get(project_id)
        if project:
            return ProjectSchema(**project)
        return None

    async def get_all(self) -> List[ProjectSchema]:
        """Retrieve all projects.
        
        Returns:
            List of project schemas.
        """
        return [ProjectSchema(**project) for project in self.projects.values()]

    async def update(self, project_id: str, project_data: UpdateProjectSchema) -> Optional[ProjectSchema]:
        """Update a project.
        
        Args:
            project_id: Project ID.
            project_data: Project update data.
            
        Returns:
            Updated project schema or None if not found.
        """
        project = self.projects.get(project_id)
        if not project:
            return None

        if project_data.name is not None:
            project["name"] = project_data.name
        if project_data.description is not None:
            project["description"] = project_data.description
        if project_data.status is not None:
            project["status"] = project_data.status
        
        project["updated_at"] = datetime.utcnow()
        return ProjectSchema(**project)

    async def delete(self, project_id: str) -> bool:
        """Delete a project.
        
        Args:
            project_id: Project ID.
            
        Returns:
            True if project was deleted, False if not found.
        """
        if project_id in self.projects:
            del self.projects[project_id]
            return True
        return False

    async def update_status(self, project_id: str, status: ProjectStatus) -> Optional[ProjectSchema]:
        """Update project status.
        
        Args:
            project_id: Project ID.
            status: New project status.
            
        Returns:
            Updated project schema or None if not found.
        """
        project = self.projects.get(project_id)
        if not project:
            return None

        project["status"] = status
        project["updated_at"] = datetime.utcnow()
        return ProjectSchema(**project)
