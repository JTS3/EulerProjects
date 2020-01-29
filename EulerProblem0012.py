#Project Euler 12  Highly divisible triangular number (http://projecteuler.net/problem=12)
#What is the value of the first triangle number to have over five hundred divisors?


def primefactorizer(a):
    factors = []
    i=2
    while i <= a:
        #print(i,a)
        if a % i==0:
            factors.append(i)
            a = a / i 
        else:
            i += 1
    return(factors)



target = 500
n = 1 
i = 1
while n < target:
#Get triangular number
    triangularnumber = int(i*(i+1)/2)
    #factor the triangular number into primes
    primefactors = primefactorizer(triangularnumber)
    n = 1
    for p in set(primefactors):
        a = primefactors.count(p)
        n = n*(a+1)
        #Count its divisors call it n
        #n = sum([triangularnumber%f==0 for f in range(1,triangularnumber+1)])
    #if the count of divisors > 500 then stop
    print(i,triangularnumber,n)
    i += 1


print("The first triangular number with", target," divisors is", i, "with", n, "factors")

