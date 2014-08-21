def prime_check(candidate_prime):
    for n in range(2,(int(candidate_prime**0.5 + 1))):
        if candidate_prime % n == 0:
            return False 
    return True

# This primechecker is basically the same as the one at the following stackoverflow link
# http://stackoverflow.com/questions/15285534/isprime-function-for-python-language


#--------------------

#Project Euler 3  largest prime factor (http://projecteuler.net/problem=3)
# The original problem specifies 600851475143 but this is more general. 

print "   "
print "This program reports the largest prime factor of a given goal number."
goal_number = input("What is the goal number?")

candidateLPF = goal_number

if prime_check(candidateLPF) == True:                         #if the number is prime then it is the Largest Prime Factor
        print candidateLPF
else:                                                        #if the candidate isn't prime...
    indexB = 2                                                #start with 2
    while indexB <= goal_number:
        if candidateLPF % indexB == 0:                         #If the candidate prime is divisible by an index number
            candidateLPF = candidateLPF / indexB              #then divide that candidate by the index number
            if prime_check(candidateLPF) == True:            #Check to see if that new number is prime
                print candidateLPF                          #if it is, then it that candidate is the Largest Prime Factor
                break
        else: indexB += 1                                   # else increment the index number and try the next number