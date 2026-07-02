from fastapi import APIRouter, Depends, HTTPException
from models import users
from sqlalchemy.orm import Session
from models.users import User
from schemas.users import UserCreate,UserResponse
from database import get_db
from utils.security import hash_password,verify_password

router =APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register",response_model=UserResponse)
def register(users:UserCreate,db:Session=Depends(get_db)):
    existing_user = db.query(User).filter((User.username == users.username) | (User.email == users.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    hashed_password = hash_password(users.password)
    new_user = User(
        username=users.username,
        email=users.email,
        hashed_password=hashed_password,
        role=users.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login",response_model=UserResponse)
def login(users:UserCreate,db:Session=Depends(get_db)):
    existing_user = db.query(User).filter((User.username == users.username) | (User.email == users.email)).first()
    if not existing_user:
        raise HTTPException(status_code=400, detail="Invalid username or email")
    
   
    if not hasattr(existing_user, 'hashed_password') or not existing_user.hashed_password:
        raise HTTPException(status_code=500, detail="Password not found in database")
    
    if not verify_password(users.password, existing_user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    return existing_user