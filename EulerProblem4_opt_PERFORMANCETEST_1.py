## PERFORMANCE TEST##

#EULER PROBLEM 4 smartest approach so far.
#ugliest code, especially on the next_palindrome algorithm
#also I started repeating myself. I will need to clean that up. 

# I FOUND ERRORS AFTER I MADE IT PRINT EACH PALINDROME
## ERRORS BEGIN AT 99099
## THE PROBLEM IS PALINDROMES WITH ODD NUMBER DIGITS


from __future__ import division
from math import ceil

#f = open('C:\Users\JTS3\Desktop\EP4RunTime.txt','w')
#f.write("factor_digits, COUNTER, factor1, factor2, largest_palindrome \n")

for a in range(8,10):
    factor_digits = a
    max_factor = (10 ** factor_digits)-1
    min_factor = 10 ** (factor_digits - 1)
    max_candidate = max_factor ** 2
    min_candidate = min_factor ** 2
    
    def first_palindrome(max_candidate):
        candidate = 0
        for n in range (0, len(str(max_candidate)) ):
            candidate += int(str(max_candidate)[0]) * 10 ** (len(str(max_candidate)) - n - 1) 
        while candidate > max_candidate:
            next_candidate = next_palindrome(candidate)
            candidate = next_candidate
        return candidate
                
    def isEven(X):
        if int(X)%2 == 0:
            return True
        else: 
            return False

    def next_palindrome(x):
        X = str(x)
        if len(X) == 1:
            next_candidate = int(X) - 1
        else:
            if isEven(len(X)):
                midpoint = int(len(X)/2)
            else:
                midpoint = int(ceil(len(X)/2))
            now_front = int(X[:midpoint])
            next_front = now_front - 1
            if len(str(now_front)) > len(str(next_front)):
                if isEven(len(X)):
                    next_candidate = int( str(next_front) + str(next_front)[midpoint-2::-1] + "9" )
                else:
                    next_candidate = int( str(next_front) + str(next_front)[midpoint-2::-1]  )
            else:
                if isEven(len(X)):
                    next_candidate = int( str(next_front) + str(next_front)[midpoint-1::-1]  )
                else: 
                    next_candidate = int( str(next_front) + str(next_front)[midpoint-2::-1]  )
        return next_candidate
    
    def scream(Ma,Mb,Mc, COUNTER):
        #s = str(factor_digits) + "," + str(COUNTER) + "," + str(Mb) + "," + str(Mc) + "," + str(Ma) 
        #f.write(s + "\n")
        print factor_digits,",", COUNTER,",", Mb,",", Mc,",",Ma
    
    candidate = first_palindrome(max_candidate)
    ENDER = 0
    COUNTER = 0
    
    while ENDER == 0:
        COUNTER += 1
    #    print "checking:", candidate
        root_cand =  candidate ** 0.5
        if root_cand  % 1 == 0:
            scream(candidate, root_cand, root_cand, COUNTER)
            b = next_palindrome(candidate)
            candidate = b
            #          print "The largest palindromic number evenly divisible into",factor_digits, "digit factors is: ", candidate," and its factors are:", root_cand,"and", root_cand 
            ENDER = 1
        else:
            for n in range( int(ceil(root_cand)), max_factor+1):
                if (candidate / n <= max_factor) & (candidate / n >= min_factor) & (candidate % n == 0):
                    scream(candidate, n, int(candidate/n), COUNTER)
    #                print "The largest palindromic number evenly divisible into",factor_digits, "digit factors is: ", candidate," and its factors are:", n,"and", int(candidate / n) 
                    ENDER = 1
            else:
                b = next_palindrome(candidate)         #clear up whether I take the output of this and reassign candidate at the end, or whether I alter a global in the function.
                candidate = b
                if candidate < min_candidate:
                    scream("NA","NA","NA",COUNTER)
                    #print " No factor was found"
                    ENDER = 1  

#f.close()