from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.services.workspace_service import get_user_workspace

router = APIRouter()

@router.get("/my-workspace")
def my_workspace(user_id: str, db: Session = Depends(get_db)):
    return get_user_workspace(db, user_id)