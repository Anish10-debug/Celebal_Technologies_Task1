import string
from pydantic import BaseModel
class Student(BaseModel):
    firstname:str
    lastname:str
    email:str
    branch:str
    batch:str