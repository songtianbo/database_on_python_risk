import sqlite3
from employee import Employee

#create the database, using :memory: for memeory only
conn = sqlite3.connect('employees.db')

c = conn.cursor()


# sqlite3 employees.db ".headers on" ".mode columns" "select * from employees";


def insert_emp(emp):
    with conn:
        if get_emps_by_name(emp.last):
            print('wtf 已经有了 can not insert', emp.first, emp.last)
        else:
            c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()
    # c.fetchone, fetchmany(n) give numbers of...


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def show_all():
    with conn:
        c.execute("""SELECT * FROM employees""")
        return c.fetchall()

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


emp_1 = Employee('Tony', 'Li', 80000)
emp_2 = Employee('Junqiang', 'Xie', 80000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Xie')
print('xie', emps)

update_pay(emp_2, 95000)
print('updated the payment ,show_all', show_all())
# remove_emp(emp_1)
remove_emp(emp_2)
# c.execute("delete from employees where employees.rowid not in (select MAX(employees.rowid) from employees group by last)")
print('removed, show_all', show_all())
# c.execute("select MAX(employees.rowid) from employees group by last")
# print('test', c.fetchall() )
emps = get_emps_by_name('Xie')
print('xie removed', emps)

conn.close()
