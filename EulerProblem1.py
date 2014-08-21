# The following responds to Problem 1 on Project Euler (https://projecteuler.net/problem=1)

top_number = input("This program gives you a list of multiples of 3 and 5 up to a given top number.  What is the top number?")
multiple_list = []
candidate_multiple = 1

while candidate_multiple < top_number:
    if candidate_multiple % (5 * 3) == 0 : multiple_list.append(candidate_multiple)
    elif candidate_multiple % 5 == 0 : multiple_list.append(candidate_multiple)
    elif candidate_multiple % 3 == 0 : multiple_list.append(candidate_multiple)
    candidate_multiple += 1

print "The multiples of 5 and 3 up to", top_number, "are:", multiple_list, "."
print "The sum of these multiples is", sum(multiple_list), "."