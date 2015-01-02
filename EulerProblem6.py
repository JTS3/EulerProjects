#Project Euler Problem 6 
#https://projecteuler.net/problem=6
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

n=100    # the highest number in the series
sumofintegers = 0
sumofsquares = 0
for i in range(1,n+1):
    sumofintegers += i
    sumofsquares += i**2

print "For the first ", n," integers,"
print "Sum of the integers:",sumofintegers
print "Sum of the sqaures :",sumofsquares
print "The difference of the squared sum and the sum of squares:", sumofintegers**2 - sumofsquares

#There is a way to futher optimize this, because the sum of a series is (n+1)n/2.  
#That can wait until later. 