#messing with arguments
#flexible arguments
#Author: Sarah Hastings

#print(1,2,3, end="\t", sep="")
print(1,2,3, sep="", end="\t")
print("hi")

#function take in a random lot of numbers
#unnamed args
def fun1(*args):
    print(type(args)) #tuple
    #print(args)
    for val in args:
        print(val)
#fun1("a","b","c") #("a","b","c") passing in abc

#keyword arguments
def fun2(**kwargs):
    print(type(kwargs))
    print (kwargs)
    #for val in args
    #   print(val)

fun2(name="joe", age=21, gender="M") #when run, its runs it as a dictionary

#sample code
def ave(*values):
    number_of_values = len(values)
    sum=0 #need something to keep adding it up
    for value in values:
        sum+=value
    average = sum/number_of_values
    return average, sum

av1, sum_of_numbers =ave(1,2,3,4,5,6)
print (f"{av1} and sum is {sum_of_numbers}")

