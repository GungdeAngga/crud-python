from pydantic import BaseModel

class User(BaseModel):
    nama: str
    alamat: str
    noHP: str

