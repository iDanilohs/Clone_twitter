# Python
from typing import Optional
from uuid import UUID
from datetime import date
from datetime import datetime
from typing import Optional, List

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# Fast API
from fastapi import FastAPI
from fastapi import status



app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ..., 
        min_length=8,
        max_length=50
        )

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
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        max_length=256,
        min_length=1
    )
    created_at: datetime = Field(
        default=datetime.now()
    )
    update_at: Optional[datetime] = Field(
        default=None
    )
    by: User = Field(...)

# Path Operations

@app.get(path="/")
def home():

    """
    Home

    This function say the welcome to the users and is the first thing to see.

    parameters:This function don't have parameters

    return the string Twitter API working in the screen
    """

    return {"Twitter API": "Working"}

## Users

@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a user",
    tags=["Users"]
    )
def signup():

    """
    Sign up

    Sign up a new user

    Parameters

    Return
    """

    pass

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
    tags=["Users"]
    )
def login():

    """
    Login

    Login a user registed

    Parameters

    Return
    """

    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
    )
def show_all_users():

    """
    Show all users

    Show all users registed

    Parameters

    Return
    """

    pass

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="show a user",
    tags=["Users"]
    )
def show_a_user():

    """
    Show a user

    Show a specific user resgisted

    Parameters

    Return
    """

    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="delete a user",
    tags=["Users"]
    )
def delete_a_user():

    """
    Delete a user

    Delete a specific user registed

    Parameters

    Return
    """

    pass

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="update a user",
    tags=["Users"]
    )
def update_a_user():

    """
    Update a user

    Upadate a specific user registed

    Parameters

    Return
    """

    pass

## Tweets