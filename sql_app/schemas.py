from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None
    
class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int
    
    class Config():
        from_attributes = True
        
class UserBase(BaseModel):
    email: str
    
class UserCreate(UserBase):
    password: str
    
class UserDelete(BaseModel):
    is_deleted: bool
    
class User(UserBase):
    id: int
    is_active: bool
    is_deleted: bool
    items: list[Item] = []
    
    class Config:
        from_attributes = True
        
class ProfileBase(BaseModel):
    full_name: str
    age: int
    
class ProfileCreate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int
    user_id: int
    
    class Config:
        from_attributes = True