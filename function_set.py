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



def json_convertion(read,data,tablename):
    head = read.read_head(tablename)
    all = []
    for j in data:
        temp = {}
        for i in range(len(head)):
            temp[head[i]] = j[i]
        all.append(temp)
    return all