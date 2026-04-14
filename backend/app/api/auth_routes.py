from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.schemas.user_schema import UserCreate, UserResponse
from app.schemas.auth_schema import LoginRequest, TokenResponse
from app.core.dependencies import get_current_user
from app.models.user import User
from app.services.auth_service import register_user, login_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return register_user(db, user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        return login_user(db, form_data.username, form_data.password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return current_user