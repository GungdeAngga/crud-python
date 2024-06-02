from fastapi import FastAPI
from routes.index import user
app = FastAPI()

app.include_router(user)
# app = FastAPI()

# @app.get("/")
# def read_somthing():
#     return{"msg":"testing app"}

