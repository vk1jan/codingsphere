from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models.project import Project
from app.schemas.project import  ProjectCreate, ProjectRead, ProjectUpdate
from app.models.user import User
from app.auth.dependencies import get_current_active_user, admin_required

router = APIRouter(prefix="/projects", tags=["projects"])

# Accessible to all users
@router.get("/", response_model=List[ProjectRead])
def read_projects(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_active_user)
):
    projects = session.exec(select(Project)).all()
    return projects

# Admin required
@router.post("/create", response_model=ProjectRead, status_code=status.HTTP_201_CREATED)
def create_project(
    project: ProjectCreate, 
    session: Session = Depends(get_session),
    current_user: User = Depends(admin_required)
):
    db_project = Project(
        name=project.name,
        description=project.description,
        user_id=current_user.id
    )
    
    session.add(db_project)
    session.commit()
    session.refresh(db_project)
    return db_project

# Admin required
@router.put("/update/{project_id}", response_model=ProjectRead)
def update_project(
    project_id: int,
    project_update: ProjectUpdate,
    session: Session = Depends(get_session),
    current_user: User = Depends(admin_required)
):
    """
    Update a project.
    Only accessible by admin role.
    """
    db_project = session.get(Project, project_id)
    if not db_project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    project_data = project_update.dict(exclude_unset=True)
    for key, value in project_data.items():
        setattr(db_project, key, value)
    
    session.add(db_project)
    session.commit()
    session.refresh(db_project)
    
    return db_project

# Admin required
@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(
    project_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(admin_required)
):
    db_project = session.get(Project, project_id)
    if not db_project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    session.delete(db_project)
    session.commit()