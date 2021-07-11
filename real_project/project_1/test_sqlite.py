import sqlite3
from employee import Employee
conn = sqlite3.connect('employee.db')
c = conn.cursor()
c.execute(
    """
    CREATE TABLE emlpyees(
        first text,
        lst text,
        pay integer
    )
    """
)


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first,:last,:pay)",
        {'first':emp.first,'last':emp.last,'pay':emp.pay})
def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last",{'last':lastname})
def update_pay(emp,pay):
    with conn:
        c.execute(
            """
            UPDATE employees SET pay = :pay
            WHERE first = :first AND last = :last
            """,
            {'first':emp.first, 'last':emp.last,'pay':pay}
        )
def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
        {'frist':emp.first,'last':emp.last})
# c.execute("INSERT INTO employees VALUE (?,?,?)",
# ('Xin','Chen',100000000000))
# conn.commit()
emp_1 = Employee('john','Doe',80000)
emp_2 = Employee('jane','Doe',70000)
conn.close()