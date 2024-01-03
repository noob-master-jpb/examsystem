from sqlite3 import *

con = connect("abc.db")

control = con.cursor()
control.execute("""drop table fun;""")