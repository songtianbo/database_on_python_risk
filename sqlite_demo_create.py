import sqlite3
from employee import Employee

#create the database, using :memory: for memeory only
conn = sqlite3.connect('employees.db')

c = conn.cursor()

# """ for doc string(huanhang)
# text interger are types

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")

conn.commit()

conn.close()
