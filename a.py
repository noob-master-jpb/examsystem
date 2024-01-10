from sqlite3 import *

con = connect("abc.db")

control = con.cursor()

control.execute("SELECT * FROM fun")
result = control.fetchall()
print(result)