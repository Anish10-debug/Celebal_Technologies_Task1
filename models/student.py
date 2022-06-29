import sqlalchemy


from sqlalchemy import Table,Column, column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta

studentDetails=Table(
    'studentDetails',meta,
    Column('ID',Integer,primary_key=True),
    Column('FirstName',String(255)),
    Column('LastName',String(255)),
    Column('Email',String(255)),
    Column('Branch',String(255)),
    Column('Batch',String(255)),
)