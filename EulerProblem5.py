#Project Euler 5  Smallest multiple (http://projecteuler.net/problem=5)
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#First get the greatest common divisor
def gcd1(inputvector):
    if len(inputvector)!=2:
        return("Error need list with 2 elements")
    if len(inputvector)==2:
        if any(inputvector)==0:
            return(inputvector)
        if any(inputvector)<0:
            return("Error Negative INputs")
        if all(inputvector)>0:
            inputvector = sorted(inputvector,reverse=True)
            bigger = inputvector[0]
            smaller = inputvector[1]
            inputvector[0] = smaller
            inputvector[1] = bigger % smaller
            return(inputvector)

def gcd(inputvector):
    if len(inputvector)!=2:
        return("Error need list with 2 elements")
    while inputvector[1]!=0:
        inputvector=gcd1(inputvector)
    return(max(inputvector))


#Get the least common multiple

def lcm(inputvector):
    if len(inputvector)!=2:
        return("Error need list with 2 elements")
    else:
        return(abs(inputvector[0]*inputvector[1])/gcd(inputvector))



#Calculate the smallest multiple

answer = 1
maxmultiple = 20
for i in range(1,maxmultiple):
    tempanswer = lcm([answer,i])
    answer = max(answer,tempanswer)

print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is ", answer)

