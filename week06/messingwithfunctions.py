#Messing with functions
#to demonstrate the defining and using functions
#view built in functions
#Author: Sarah Hastings

#x,y,z= (1,2,3) #define 3 variables in a row

#print (x,y,z) # sep="" if dont want a space or what want to divide by, end="" if dont want a new line
#print (1,2,3)
#print (f"{x}-{y} {z}") #print taking in 1 arugment which is a formatted string
#print ("{} {} {}".format(x,y,z))

#def cube(number):
def topower(number,power=3):
    #print(number)
    #return(number ** 3)
    return(number ** power)

#ans = cube(23)
#print(f"we got {ans}")
num=45 #make it a variable
print(f"and {num} is {topower(num,3)}") #{topower(num,3)}") can use 2 for power of 2 {topower(num,2)}") if dont pass in any value, will default to 3