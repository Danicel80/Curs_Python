import sqlite3

con = sqlite3.connect("marketplace.db")
print(con)
cursor = con.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price TEXT NOT NULL,
    stock_count INTEGER DEFAULT 1,
    description TEXT
    );
    """
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES users (id)
    );
    """
)

username = "maricica"
email = "maricica@f.com"
password = "666"

# user_sql = """
# INSERT INTO users (username, email, password)
# VALUES (?, ?, ?);
# """
# cursor.execute(user_sql, (username, email, password))

# user_sql = f"""
#             INSERT INTO users (username, email, password)
#             VALUES ('{username}', '{email}', '{password}');
#             """
#
# cursor.execute(user_sql)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for table_name in tables:
    print(table_name[0])


con.commit()

con.close()
