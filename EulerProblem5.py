candidate_number = 2520
bottom_number = 1
top_number = 10
n = bottom_number


while n <= top_number:
    if candidate_number % n <> 0:
        print "NO!", candidate_number, "divided by", n, "has a remainder!"
        break
    else:
        print n  #comment this out later
        n += 1   
if n > top_number:
     print "success" 