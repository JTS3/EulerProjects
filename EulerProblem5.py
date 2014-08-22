def MultipleCheck(local_n,local_top_number,local_candidate_number):
    while local_n <= local_top_number:
        if local_candidate_number % local_n <> 0:
#            print "NO!", local_candidate_number, "divided by", local_n, "has a remainder!"
            break
        else:
            print local_candidate_number, local_n  #comment this out later
            local_n += 1  
        if local_n > local_top_number:
            print "success", local_candidate_number 
            global ENDER
            ENDER = 1 

# Since we know that 2520 is that smallest number divisible by all numbers from 1 to 10, we know that the candidate number must exceed 2520

candidate_number = 2520  
bottom_number = 2   # this does not have to start at 1. It is obvious that N%1 = 0 for all N. 
top_number = 20
ENDER = 0

while ENDER == 0:
    MultipleCheck(bottom_number, top_number, candidate_number)
    candidate_number += 1
