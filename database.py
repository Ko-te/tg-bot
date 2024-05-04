# from pydantic import BaseModel
#
# class Item(BaseModel):
#     name: str
#     description: str
#     price: float
#
# pizza = [
#     Item(**{
#         'name': 'Margharita',
#         'description': 'pizza with tomato, cheese and tomato sauce',
#         'price': 15.99
#     }),
#     Item(**{
#         'name': 'Four Seasons',
#         'description': 'pizza with tomato, cheese and tomato sauce',
#         'price': 19.99
#     })
# ]


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://shrek:qwerty123@92.53.124.106:3306/pizza_shop")
SessionLocal = sessionmaker(autoflush=False, bind=engine)

db = SessionLocal()
Base = declarative_base()