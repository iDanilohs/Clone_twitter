# Python
from typing import Optional
from uuid import UUID
from datetime import date
from typing import Optional

# Pydantic
from pydantic import BaseModel

# Fast API
from fastapi import FastAPI
from pydantic import EmailStr
from pydantic import Field

app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ..., 
        min_length=8)

class User(UserBase):
    
    firs_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    birth_date: Optional[date] = Field(default=None)

class Tweet(BaseModel):
    pass

@app.get(path="/")
def home():

    """
    Home

    This function say the welcome to the users and is the first thing to see.

    parameters:This function don't have parameters

    return the string Twitter API working in the screen
    """

    return {"Twitter API": "Working"}