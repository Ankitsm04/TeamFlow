from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.core.security import hash_password, verify_password, create_access_token

def register_user(db: Session, user: UserCreate):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise Exception("Email already registered")
    
    hashed_password = hash_password(user.password)

    new_user = User(
        email = user.email,
        password = hashed_password,
        is_verified = True,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password, user.password):
        raise Exception("Invalid credentials")

    token = create_access_token({"sub": str(user.id)})

    return {"access_token": token}