from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User
from sqlalchemy.sql import select

user = APIRouter()

@user.get("/")
async def read_data():
    result = conn.execute(select(users)).mappings().all()
    return result

@user.get("/{id}")
async def read_data(id: int):
    result = conn.execute(select(users).where(users.c.id == id)).mappings().all()
    return result

@user.post("/")
async def write_data(user: User):
    conn.execute(users.insert().values(
        nama=user.nama,
        alamat=user.alamat,
        noHP=user.noHP
    ))
    result = conn.execute(select(users)).mappings().all()
    return result

@user.put("/{id}")
async def update_data(id: int, user: User):
    conn.execute(users.update().values(
        nama=user.nama,
        alamat=user.alamat,
        noHP=user.noHP
    ).where(users.c.id == id))
    result = conn.execute(select(users)).mappings().all()
    return result

@user.delete("/{id}")
async def delete_data(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    result = conn.execute(select(users)).mappings().all()
    return result
