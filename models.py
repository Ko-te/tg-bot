from sqlalchemy import Column, Integer, String, Text, DECIMAL
from database import Base


class Pizza(Base):
    __tablename__ = 'pizzas'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(DECIMAL(10, 2), nullable=False)