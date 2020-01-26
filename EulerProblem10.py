#Project Euler 10  Summation of primes (http://projecteuler.net/problem=10)
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
outputsum = 17 #initial value, the sum of the primes less than 10
for i in range(11,maxrange,2):
    if(isprime(i)):
        outputsum += i

print("The sum of the primes below", maxrange,"is", outputsum)

#This way seems to take too long. There is probably a simpler way. 
    #I cut out the evens by starting at 11 and walking through the range 2 steps at a time. Obvious. 
    #It's the prime checker that takes most of the time. 
    #I think it is the all() statement that takes too much time, also all the if() statements.
#The answer is: The sum of primes below 2,000,000 is 142,913,828,922. 