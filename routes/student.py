from fastapi import APIRouter
from models.index import studentDetails
from config.db import conn
from schema.student import Student
student=APIRouter()

@student.get("/")
async def read_data():
    return conn.execute(studentDetails.select()).fetchall()

@student.get("/{id}")
async def read_data(id: int):
    return conn.execute(studentDetails.select().where(studentDetails.c.ID==id)).fetchall()

@student.post("/")
async def write_data(student:Student):
    conn.execute(studentDetails.insert().values(
        FirstName=student.firstname,
        LastName=student.lastname,
        Email=student.email,
        Branch=student.branch,
        Batch=student.batch
    ))
    return conn.execute(studentDetails.select()).fetchall()

@student.delete("/{id}")
async def delete_data(id:int):
    conn.execute(studentDetails.delete().where(studentDetails.c.ID==id))
    return conn.execute(studentDetails.select()).fetchall()

@student.put("/{id}")
async def update_data(id:int,student:Student):
    conn.execute(studentDetails.update().values(
        FirstName=student.firstname,
        LastName=student.lastname,
        Email=student.email,
        Branch=student.branch,
        Batch=student.batch
    ).where(studentDetails.c.ID==id))
    return conn.execute(studentDetails.select()).fetchall()