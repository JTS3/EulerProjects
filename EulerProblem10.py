#Project Euler 10  sum of the primes (http://projecteuler.net/problem=10)
#Find the sum of all the primes below two million

#check for prime
def isprime(a):
    if(a<0):
        return("Error Negative input!")
    if(a==0):
        return(False)
    if(a==1):
        return(False)
    if(a==2 or a==3):
        return(True)
    if(a>2 and a%2==0):
        return(False)
    if(a>2 and a%2!=0):
        maxfactor = int(a**0.5)+1
        return(all([a%x for x in range(2,maxfactor+1)])!=0)


maxrange = 2*10**6
outputsum = 0 #initial value
for i in range(2,maxrange,1):
    if(isprime(i)):
        outputsum += i

print("The sum of primes below", maxrange,"is", outputsum)

#This way seems to take too long. There is probably a simpler way. 