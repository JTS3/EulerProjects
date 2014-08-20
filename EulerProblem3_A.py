def PrimeCheck(CandidatePrime):
    for n in range(2,(int(CandidatePrime**0.5 + 1))):
        if CandidatePrime % n == 0:
            return False 
    return True

# This primechecker is basically the same as the one at the following stackoverflow link
# http://stackoverflow.com/questions/15285534/isprime-function-for-python-language


#--------------------

#Project Euler 3  largest prime factor (http://projecteuler.net/problem=3)
# The original problem specifies 600851475143 but this is more general. 

print "This program reports the largest prime factor of a given goal number."
GoalNumber = input("What is the goal number?")

CandidateLPF = GoalNumber

if PrimeCheck(CandidateLPF) == True:                         #if the number is prime then it is the Largest Prime Factor
        print CandidateLPF
else:                                                        #if the candidate isn't prime...
    IndexB = 2                                                #start with 2
    while IndexB <= GoalNumber:
        if CandidateLPF % IndexB == 0:                         #If the candidate prime is divisible by an index number
            CandidateLPF = CandidateLPF / IndexB              #then divide that candidate by the index number
            if PrimeCheck(CandidateLPF) == True:            #Check to see if that new number is prime
                print CandidateLPF                          #if it is, then it that candidate is the Largest Prime Factor
                break
        else: IndexB += 1                                   # else increment the index number and try the next number
