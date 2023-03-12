#generate primes
#Author: Sarah Hastings
primes = [] #store in a list, if find primes put into list
upto = 1001
for candidate in range (2, upto):
    #print (candidate)
    isPrime = True
    #only need to check if divisable by prime. if divisable by an int it is not a prime number, so no reason to keep checking
    for divisor in range (2,candidate): #candidate is number we are checking
        if (candidate % divisor == 0):
            isPrime = False
            break
    if isPrime:
        primes.append(candidate)
    
print(primes)