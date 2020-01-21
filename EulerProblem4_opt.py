# This responds to Problem4 on Project Euler  
# ( http://projecteuler.net/problem=4 )
# The problem asks for the largest palindromic number that is the product of two three digit numbers. 

from math import ceil


#This defines the range of numbers in which we should look
factor_digits = int(input("How many digits are in the factor?"))
max_factor = (10 ** factor_digits)-1
min_factor = 10 ** (factor_digits - 1)
max_range = max_factor ** 2
min_range = min_factor ** 2


#What are the palindromes?
def PalindromeCheck(candidate_palindrome):
    indexA = 0
    indexB = len(str(candidate_palindrome))
    while indexA < indexB:
        if str(candidate_palindrome)[indexA] == str(candidate_palindrome)[(indexB - 1)-indexA]:
            indexA += 1
        else:
            return False 
            break
    if indexA == indexB:
        return True

candidates = []
for n in range(min_range, max_range):
    if PalindromeCheck(n):
        candidates.append(n)


#Work backwards through the list of palindromes to get the largest palindrome that can be broken into two three digit factors

ENDER = 0
while ENDER == 0:
    #Get the largest of the candidate palindromes.
    max_candidate = max(candidates)
    #What are the pairs of factors in the range(min_factor,max_factor) of that max_candidate?
    for n in range(max_factor,min_factor-1,-1):
        if max_candidate % n == 0  and max_candidate/n >= min_factor and max_candidate/n <=max_factor:
                print("Palindrome",max_candidate, "is divisible into ", n," and ", max_candidate/n)
                ENDER=1
                break
    #print(max_candidate)
    candidates.remove(max_candidate) #Remove that max_candidate and move on






