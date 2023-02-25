from pydantic import BaseModel


class UserInput(BaseModel):

    name: str 
    email: str
    password: str 
    confirm_pass: str


class UserOutput(BaseModel):

    name: str 
    email: str
    password: str 
    confirm_pass: str
