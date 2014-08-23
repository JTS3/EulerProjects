#EULER PROBLEM 4 smartest approach so far. 
#optimizes on search time, I think. 



factor_digits = input("How many digits are in the factor?")
max_factor = (10 ** factor_digits)-1
min_factor = 10 ** (factor_digits - 1)
max_candidate = max_factor ** 2
min_candidate = min_factor ** 2

#TO DO LIST
#create first_palindrome
#   This must generate a palindrome less than max_candidate 

#create next_palindrome(candidate)
#   This must take the current palindrome alter the central digits in such a way to produce the next lowest palindrome.

#sketch of the main body of the program. 

#
# candidate = first_palindrome
# 
# while ENDER == 0:
#     root_cand =  candidate ** 0.5
#     if root_cand  is an integer:
#          print candidate, root_cand, root_cand , "THIS!"
#          ENDER = 1
#     else:
#         for n in range( cieling(root_cand), max_factor):
#             if (candidate / n < max_factor) & (candidate % n == 0):
#                   print candidate, n, (candidate / n) , "THIS!"
#                   ENDER = 1
#     next_palindrome(candidate)         #clear up whether I take the output of this and reassign candidate at the end, or whether I alter a global in the function. 
#     if candidate < min_candidate:
#           print " No factor was found"
#           ENDER = 1
