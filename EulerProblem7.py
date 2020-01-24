#Project Euler 7  10001st prime (http://projecteuler.net/problem=7)
#10001st prime

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


#Get the 10,001th prime

i = 1
n = 1
theprimeyouwant = 10001
while i <= theprimeyouwant:
    if isprime(n):
        if i == theprimeyouwant:
            print("The ",i,"th prime is",n)
        i += 1
    n += 1