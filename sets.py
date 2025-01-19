#Immutable Unordered Collections

my_set = {3, 6, "cat", 4.5, False}

#Length
print(f"Length of the set: {len(my_set)}")

#Membership
y = 4 in my_set
print(f"Is 4 in the set: {y}")

new_set = {True, "dog", 3, 9, 12.5}

# set1 | set2 returns a new set with all elements from both sets
print(f"| operation: {my_set | new_set}")

# set1 & set2 returns a new set with only elements common to both sets
print(f"& operation: {my_set & new_set}")

#set1 - set2 returns a new set with all items from the first set not in second
print(f"- operation: {my_set - new_set}")

#set1 <= set2 asks whether all the elements of the first set are in the second
print(f"<= operation: {my_set <= new_set}")
