#messingwithnumbers
#reusing code
#Author: Sarah Hastings

def readNum(message="enter a number: "):
    num = False
    while(num == False):
        try:
            num = int(input(message))
        except ValueError:
            print("that was not a number", end="") 
    return num 

num1 = readNum()
num2 = readNum("enter num2 ")

answer = num1 * num2

print(f" answer is {answer}")

#above is a simple program
#instead of (num1 ==False) can say (not num)