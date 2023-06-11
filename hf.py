#Reversing tuples
my_tuples = (1, 2, 2, 3, 4, 4, 4, 5)
print("The content of my_tuple is:")
print(my_tuples)
print("Reversing the tuple: ")
rev_tuple = tuple(reversed(my_tuples))
print('The content of rev_tuple is:')
print(rev_tuple)
print(f"The number of 4 in this tuple:{rev_tuple.count(4)}")