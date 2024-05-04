from sqlalchemy import create_engine, text
# import pymysql

connection_string = "mysql+pymysql://student:qwertyuiop@92.53.124.106:3306/pizza_shop"
engine = create_engine(connection_string)
# connection = engine.connect()

with engine.connect() as connection:
    result_ = connection.execute(text("SELECT id, name, description, price FROM pizzas;"))

result = [item for item in result_]

for item in result:
    print(f'|| Id: {item[0]:<6}|| Pizza: {item[1]:<20}|| Description: {item[2]:<40}|| Price: {item[3]:<10}||')

