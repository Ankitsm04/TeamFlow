from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.workspace import Workspace

def get_user_workspace(db: Session, user_id):
    
    workspace = db.query(Workspace).filter(
        Workspace.owner_id == user_id
    ).first()

    if not workspace:
        raise HTTPException(status_code=404, detail="Workspace not found")

    return workspace