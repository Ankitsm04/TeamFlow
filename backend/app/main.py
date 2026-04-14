from fastapi import FastAPI, Depends
from app.db.database import Base, engine

from app.api.auth_routes import router as auth_router

app = FastAPI(title="TeamFlow Backend APIs")

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "TeamFlow API running!"}
