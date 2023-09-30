from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True 
        
'''
Pydantic's from_attributes will tell the Pydantic model
to read the data even if it is not a dict, but an ORM model
(or any other arbitrary object with attributes)
'''

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    
class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        from_attributes = True

