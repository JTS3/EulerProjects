#Project Euler 6  Sum square difference (http://projecteuler.net/problem=6)
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

n = 100
inputvector = range(1,n+1,1)  #the plus one is an annoyance driven by 0-indexing
inputvector = [x * 1 for x in inputvector]
squaredsum = sum(inputvector)**2
inputvector = [x ** 2 for x in inputvector]
sumofsquares = sum(inputvector)
answer = sumofsquares - squaredsum 

print("The difference between the squared sum and the square of the sum for the first",n,"natural numbers is", answer)

#This is easier to write in R.