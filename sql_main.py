from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:////Users/LEXX/PycharmProjects/Curs_Python/marketplace.db', echo=True)


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    username = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sesiune = Session()

new_user = Users(username="marioara", email="marioara@f.com", password="4242")
sesiune.add(new_user)
sesiune.commit()

user_list = [
    {
        "username": "x",
        "email": "x@f.com",
        "password": "123"
    },
    {
        "username": "y",
        "email": "y@f.com",
        "password": "333"
    },
    {
        "username": "z",
        "email": "z@f.com",
        "password": "666"
    }
]

# for element in user_list:
#     user = Users(**element)
#     sesiune.add(user)
# sesiune.commit()

all_entries = sesiune.query(Users).all()

for user in all_entries:
    print(f"{user.username}, {user.email}")

users = sesiune.query(Users).filter_by(email="y@f.com").all()
for user in users:
    print(user.username, user.email, user.password)

# session.query(Users).all()



# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS facultati(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nume_facultate TEXT NOT NULL,
#     );
#     """
# )
#
# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS products(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     category TEXT NOT NULL,
#     price TEXT NOT NULL,
#     stock_count INTEGER DEFAULT 1,
#     description TEXT
#     );
#     """
# )
#
# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS orders(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     customer_id INTEGER NOT NULL,
#     order_date TEXT,
#     FOREIGN KEY (customer_id) REFERENCES users(id)
#     );
#     """
# )
# username = ""
# email = ""
# password = ""
#
# user_sql = f"""
# INSERT INTO users (username, email, password, ...)
# VALUES ({username}, {email}, {password}, ...);
#
# """
# cursor.execute(user_sql)



