#They are immutable ordered collections

my_tuple = (2, True, 4.96, 'memory')

#Length
print(f"Length of the tuple: {len(my_tuple)}")

#Repetition
new_tuple = my_tuple*3
print(f"Repetition: {new_tuple}")

#Indexing
print(f"Item at index 2: {my_tuple[2]}")

#Slicing
print(f"slicing: {my_tuple[1:3]}")

#Concatenation
concat_tuple = new_tuple+my_tuple
print(f"Concatenation: {concat_tuple}")

#Membership
membership = 4.96 in my_tuple
print(f"Is 4.96 in my tuple?: {membership}")
