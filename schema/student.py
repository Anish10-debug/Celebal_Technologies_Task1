from pydantic import BaseModel
class Student(BaseModel):
    firstname:str
    lastname:str
    email:str
    branch:str
    batch:str

class SignIn(BaseModel):
    username:str
    password_user:str