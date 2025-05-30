from typing import Optional, List, Dict
from fastapi import APIRouter, Depends, Query, Path, Body
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db import db_user
from db.database import get_db
from schemas import UserBase, UserDisplay

router = APIRouter(prefix="/user", tags=["user"])


# Create User
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# Read all users
@router.get("/", response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


# Read user
@router.get("/{id}", response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, id)


# Update user
@router.post("/{id}/update")
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, id, request)


# Delete user
@router.get("/delete/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, id)
