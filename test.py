from database_api import *

r = Reader("database.db")
a =''

for i in r.personal_data("john_doe"):
    for j in i:
        a += ' ' + str(j)
print(a)