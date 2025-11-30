from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .database import Base

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column()
    is_active: Mapped[bool] = mapped_column(default=True)
    is_deleted: Mapped[bool] = mapped_column(default=False)
    
    items = relationship('Item', back_populates='owner', cascade="all, delete-orphan")
    profile = relationship("Profile", back_populates="user", uselist=False)
    
    
class Item(Base):
    __tablename__ = 'items'
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(index=True)
    description: Mapped[str] = mapped_column(index=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    
    owner = relationship('User', back_populates='items')

class Profile(Base):
    __tablename__ = 'profile'
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(index=True)
    age: Mapped[int] = mapped_column(index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    
    user = relationship('User', back_populates='profile')