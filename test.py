class MyList:
    # def __init__(self, data):
    #     self.data = data
    
    def __getitem__(self, index):
        return {1:2,2:5}[index]

# Example usage
my_list = MyList()
# print(my_list[0:2])  # Output: 1
print(my_list[2])  # Output: 3
