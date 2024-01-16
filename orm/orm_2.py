import sqlalchemy
from sqlalchemy.orm import sessionmaker

from orm_1 import Publisher, Shop, Book, Stock, Sale

DSN = "postgresql://postgres:postgres@localhost:5432/book_sales_db"
engine = sqlalchemy.create_engine(DSN)

# сессия
Session = sessionmaker(bind=engine)
session = Session()


# запрос

# user_input = input("Введите имя издателя: ")
q = session.query(Sale).join(Stock.sale)
    # .join(Stock.id_book).join(
    #     Shop.id).join(Sale.id_stock).filter(
    #         Publisher.name == user_input)
print(q)
for s in q.all():
    print(s.price, s.id_book)
