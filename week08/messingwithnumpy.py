#messingwithnumpy
#Author: Sarah Hastings


import numpy as np
list_of_numbers = [1,2,3,5, "asdf"]
list_of_numbers = list_of_numbers + [3] #add number to end of list
print("list", list_of_numbers)

numbers = np.array([1,2,3,4]) #this defines it
numbers = numbers * [1,2,3,4]
print("array", numbers)

rando = np.random.randint(100,200,30) #30 random int between 100 and 200

print(rando)
normalrando = np.random.normal(loc=50, scale=20, size=100)
print(normalrando)