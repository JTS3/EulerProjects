# -*- coding: utf-8 -*-
def PalindromeCheck(candidate_palindrome):
    indexA = 0
    indexB = len(candidate_palindrome)
    while indexA < indexB:
        if candidate_palindrome[indexA] == candidate_palindrome[(indexB - 1)-indexA]:
            indexA += 1
        else:
            return False 
            break
    if indexA == indexB:
        return True


def Scream(Ma, Mb, Mc):
    print "The largest palindromic number that is a product of two", len(str(Ma)),"digit numbers is", Mc, "."
    print "The relevant numbers are", Ma,"and", Mb, "."


def roll_through(Ra, Rb, Rinc):
    while Ra >= Rinc:
        Rproduct = Ra * Rb
        if PalindromeCheck(str(Rproduct)) == True:
            Scream(Ra, Rb, Rproduct)
            global ENDER 
            ENDER = 1
            break
        else:
            Ra += -1


# This responds to Problem4 on Project Euler  
# ( http://projecteuler.net/problem=4 )
# The problem asks for the largest palindromic number that is the product of two three digit numbers. 
# This can also be used more generally by adjusting the starting numbers and the inclusive lower bound. 


# I still need to verify that this produces the correct output.
# But it looks right. 
# I also need to adjust the variable names to reflect naming conventions. 
# I also used a global variable and I read that this is discouraged. 


ENDER = 0
startA = 999
startB = 999
inclusive_lower_bound = 100

factorA = startA
factorB = startB

while ENDER == 0:
    roll_through(factorA, factorB, inclusive_lower_bound)
    factorB += -1
    factorA = startA