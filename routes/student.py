from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from models.index import studentDetails
from models.index import signin
from config.db import conn
from schema.student import Student
from schema.student import SignIn
from passlib.hash import bcrypt
import jwt


student=APIRouter()
oauth2_scheme= OAuth2PasswordBearer(tokenUrl='check_auth')


@student.post("/signIn")
async def sign_up(sign:SignIn):
    
    conn.execute(signin.insert().values(
        Username=sign.username,
        Password_User=bcrypt.hash(sign.password_user)
    ))
    return conn.execute(signin.select().where(signin.c.Username==sign.username)).fetchall()

@student.post('/check_auth')
async def check_authentication(form_data: OAuth2PasswordRequestForm=Depends()):
    user=await authenticate_user(form_data.username,form_data.password)

    if not user:
        return {'Invalid username/password'}
    else:
        # token=jwt.encode(user[0].dict(),JWT_SECRET)
        # return {'access-token':token}
        return{'Valid'}

def verify_password(password:str,hashed_pass:str):
    return bcrypt.verify(password,hashed_pass)

async def authenticate_user(username:str,password:str):
    user= conn.execute(signin.select().where(signin.c.Username==username)).fetchall()
    if not user:
        return False
    else:
        if(verify_password(password,user[0][2])):
            return user
        else:
            return False


@student.get("/")
async def read_data(user: str= Depends(oauth2_scheme)):
    return conn.execute(studentDetails.select()).fetchall()

@student.get("/{id}")
async def read_data(id: int,user: str= Depends(oauth2_scheme)):
    return conn.execute(studentDetails.select().where(studentDetails.c.ID==id)).fetchall()

@student.post("/")
async def write_data(student:Student,user: str= Depends(oauth2_scheme)):
    conn.execute(studentDetails.insert().values(
        FirstName=student.firstname,
        LastName=student.lastname,
        Email=student.email,
        Branch=student.branch,
        Batch=student.batch
    ))
    return conn.execute(studentDetails.select()).fetchall()

@student.delete("/{id}")
async def delete_data(id:int,user: str= Depends(oauth2_scheme)):
    conn.execute(studentDetails.delete().where(studentDetails.c.ID==id))
    return conn.execute(studentDetails.select()).fetchall()

@student.put("/{id}")
async def update_data(id:int,student:Student,user: str= Depends(oauth2_scheme)):
    conn.execute(studentDetails.update().values(
        FirstName=student.firstname,
        LastName=student.lastname,
        Email=student.email,
        Branch=student.branch,
        Batch=student.batch
    ).where(studentDetails.c.ID==id))
    return conn.execute(studentDetails.select()).fetchall()