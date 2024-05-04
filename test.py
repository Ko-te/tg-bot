from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from database import db


app = FastAPI()
templates = Jinja2Templates(directory="templates")


# class Item(BaseModel):
#     name: str
#     description: str
#     price: float


# @app.get("/product")
# def get_product(request: Request, name: str):
#     for item in pizza:
#         if item.name == name:
#             return templates.TemplateResponse("index.html", {"request": request, "data": item})
#
#     return {'message': 'Not found'}


@app.get("/pizzas")
def read_all_pizzas(request: Request):
    return templates.TemplateResponse("table.html", {"request": request})