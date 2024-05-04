from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPAuthorizationCredentials
# from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel
# from typing import List


app = FastAPI()
security = HTTPBasic()


class U(BaseModel):
    amount: int
    price: int
    name: str
    caregory: str


sample_product_1 = {

    "product_id": 123,
    "name": 'Smartphone',
    "category": 'Smartphone',
    "price": 599.99

}

sample_product_2 = {

    "product_id": 234,
    "name": "Phone case",
    "category": "Case",
    "price": 12.99

}


sample_products = [sample_product_1, sample_product_2]


@app.get("/product/{product_id}")
def get_product_info(product_id: int):
    for item in sample_products:

        if item.get("product_id") == product_id:

            return item

        # return [product for product in sample_products]

    return {"message": "Указанного вами товара не существует"}


# def is_user(user_data: HTTPAuthorizationCredentials = Depends(security)):
#     if user_data.username == 'Admin' and user_data.password == '1234':
#         return user_data.username
#
#     elif user_data.username == 'Admin2' and user_data.password == '4321':
#         return user_data.username
#
#     raise HTTPException
#
#
# @app.get("/root")
# def admin_auth(user_name: str = Depends(is_user)):
#
#     return PlainTextResponse(f'Hello, {user_name}!')
