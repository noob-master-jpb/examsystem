import random
import json
from sqlite3 import *

con = connect('database.db')
cur = con.cursor()


# binary data convertion(and vice-versa) section
def data_to_bin(filename):
    with open(filename,'rb') as file:
        data = file.read()
        return data
    
def bin_to_data(filename,data):
    with open(filename,'wb') as file:
        file.write(data)
        
# otp genarator

def otp(digits = 4):
    try:
        return random.randrange(10**(digits-1), 10**(digits)-1)
    except:
        print("Error occured!. Using Default values")
        return random.randrange(10**(4-1), 10**(4)-1)

# jason section
 
def load_json(filename):
    with open(filename) as file:
        data = json.load(file)
        return data
    
# log section

def log(filename,data):
    with open(filename,'a+') as file:
        file.write(data+'\n')

a = [(1, '2024-01-15', '09:00:00', '12:00:00', '03:00:00', 'sem1'), 
     (4, '2024-03-10', '09:00:00', '12:00:00', '03:00:00', 'sem2'), 
     (5, '2024-03-25', '13:30:00', '16:30:00', '03:00:00', 'sem3'), 
     (2, '2024-02-01', '10:30:00', '13:30:00', '03:00:00', 'sem4'), 
     (3, '2024-02-15', '14:00:00', '17:00:00', '03:00:00', 'sem5')]
cur.execute("PRAGMA table_info(exam_schedule);")
head = [i[1] for i in cur.fetchall()]
all = []
for j in a:
    temp = {}
    for i in range(len(head)):
        
        temp[head[i]] = j[i]
    # print(temp)
    all.append(temp)
# print(exams)
for i in all:
    print(i)
    

# a = [i for i in range(0,2)]