from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id, models.User.is_deleted == False).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    facked_hashed_password = user.password + 'notrealy'
    db_user = models.User(email = user.email, hashed_password = facked_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.model_dump(), owner_id = user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_user_item(db: Session, user_id: int, update_data: schemas.ItemBase):
    item = db.query(models.Item).filter(models.Item.owner_id == user_id).first()
    item.title = update_data.title
    item.description = update_data.description
    db.commit()
    db.refresh(item)
    return item

def update_user_email(db: Session, user_id: int, update_data: schemas.UserBase):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    user.email = update_data.email
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user: models.User):
    db.delete(user)
    db.commit()
    
