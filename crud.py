from sqlalchemy.orm import Session
from models import Pizza


def read_pizzas(db: Session):
    try:
        items = db.query(Pizza).all()
    except:
        print('ошибка получения данных')

    return items

def delete_pizza(db: Session, item_id:int):
    try:
        items = db.query(Pizza).filter(Pizza.id == item_id).one()
        db.delete(item)
        db.commit()
        db.refresh()
    except:
        print('Delete error')




