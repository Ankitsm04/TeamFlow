from sqlalchemy.orm import Session
from app.models.user import User
from app.models.otp_model import OTP
from datetime import datetime, timedelta, timezone
from app.schemas.user_schema import UserCreate
from app.core.security import hash_password, verify_password, create_access_token
from app.utils.otp_utils import generate_otp, hash_otp
from app.utils.email_service import send_otp_email
from fastapi import HTTPException
from app.models.workspace import Workspace

def register_user(db: Session, user: UserCreate):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise Exception("Email already registered")
    
    hashed_password = hash_password(user.password)

    new_user = User(
        email = user.email,
        password = hashed_password,
        is_verified = False,
    )

    db.add(new_user)
    db.commit()

    otp = generate_otp()
    print(otp)
    hashed = hash_otp(otp)

    expires_at = datetime.now(timezone.utc) + timedelta(minutes=5)

    existing = db.query(OTP).filter(OTP.email == user.email).first()
    if existing:
        db.delete(existing)
        db.commit()
    
    db.add(OTP(
        email = user.email,
        otp = hashed,
        expires_in = expires_at
    ))

    db.commit()

    send_otp_email(user.email, otp)

    return {
        "message": "User registered.Please verify OTP",
        "email": user.email
    }

def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password, user.password):
        raise Exception("Invalid credentials")
    
    if not user.is_verified:
        raise Exception("Please verify your email first")

    token = create_access_token({"sub": str(user.id)})

    return {"access_token": token}

def verify_user_otp(db: Session, email: str, otp: str):
    
    record = db.query(OTP).filter(OTP.email == email).first()

    if not record:
        raise HTTPException(status_code=400, detail="OTP not found")

    if record.expires_in < datetime.utcnow():
        raise HTTPException(status_code=400, detail="OTP expired")

    if hash_otp(otp) != record.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_verified = True

    existing_workspace = db.query(Workspace).filter(
        Workspace.user_id == user.id
    )

    if not existing_workspace:
        workspace = Workspace(
            name="Default Workspace",
            user_id = user.id
        )
        db.add(workspace)

    db.delete(record)
    db.commit()

    return {
        "message": "Email verified successfully"
    }

def resend_otp(db: Session, email: str):

    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.is_verified:
        raise HTTPException(status_code=400, detail="User already verified")

    otp = generate_otp()
    hashed = hash_otp(otp)

    expires = datetime.utcnow() + timedelta(minutes=5)

    record = db.query(OTP).filter(OTP.email == email).first()

    if record:
        record.otp = hashed
        record.expires_in = expires
    else:
        db.add(OTP(
            email=email,
            otp=hashed,
            expires_in=expires
        ))

    db.commit()

    send_otp_email(email, otp)

    return {
        "message": "OTP sent again successfully"
    }