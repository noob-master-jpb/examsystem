import random
import json

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

