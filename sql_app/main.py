from fastapi import FastAPI, Depends, HTTPException
from .database import engine, SessionLocal
from . import models, schemas, crud
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        
@app.post('/users/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db= db, email = user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email is already registered')
    return crud.create_user(db=db, user=user)

@app.get('/users/', response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users
 
@app.get('/users/{user_id}', response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db=db, user_id=user_id)
    return user
    
@app.post('/users/{user_id}/items', response_model=schemas.Item)
def create_items(user_id: int,item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, user_id=user_id, item=item)

@app.get('/items/', response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db=db, skip=skip, limit=limit)
    return items


@app.patch('/update_email/{user_id}', response_model=schemas.User)
def update_user_email(user_id: int, new_email: schemas.UserBase, db: Session = Depends(get_db)):
    return crud.update_user_email(db=db, user_id=user_id, update_data=new_email)

@app.delete('/delete_user/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
       raise HTTPException(status_code=400, detail='User not found')
    crud.delete_user(db=db ,user=user)
    return 'User was deleted'
     
@app.post('/users/{users_id}/profile')
def create_profile(users_id: int, profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
    db_profile = crud.get_profile(db=db, id = users_id)
    if db_profile:
        raise HTTPException(status_code=400, detail='Profile is already registered')
    return crud.create_profile(db=db, user_id=users_id, profile=profile)

@app.get('/profile')
def read_profile(user_id: int, db: Session = Depends(get_db)):
    return crud.get_profile(db=db, id=user_id)

@app.patch('/items/{user_id}')
def update_item(user_id: int, new_item: schemas.ItemBase, db: Session = Depends(get_db)):
    return crud.update_user_item(db=db, user_id=user_id, update_data=new_item)

@app.patch('/users/{user_id}/soft_delete', response_model=schemas.User)
def update_user_soft_delete(user_id: int, new_deleted: schemas.UserDelete, db: Session = Depends(get_db)):
    return crud.update_soft_delete(db=db, user_id=user_id, new_deleted=new_deleted)