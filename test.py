all = []

ctrl = 1


while ctrl:
    print('something')
    while True:
        temp = {}
        name = input('enter name: ')
        if name == 'stop':
            ctrl = 0
            break
            
        Class = input('enter class: ')
        if Class == 'stop':
            ctrl = 0
            break
            
        temp['name'] = name
        temp['class'] = Class
        all.append(temp)
    print('anything')
    
print(all)