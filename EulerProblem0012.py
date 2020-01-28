#Project Euler 12  Highly divisible triangular number (http://projecteuler.net/problem=12)
#What is the value of the first triangle number to have over five hundred divisors?


target = 500
n = 0 
i = 1
while n < target:
#Get triangular number
    triangularnumber = i*(i+1)/2
    #Count its divisors call it n
    n = sum([i%f==0 for f in range(1,i+1)])
    #if the count of divisors > 500 then stop
    i += 1

print("The first triangular number with", target," divisors is", i, "with", n, "factors")


#This will do the job but it is slow. 
