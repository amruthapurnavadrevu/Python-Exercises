#Immutable Unordered Collections

my_set = {3, 6, "cat", 4.5, False}

#Operators

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

#Methods

#Union, |
print(f"Union: {my_set.union(new_set)}")

#Intersection, &
print(f"Intersection: {my_set.intersection(new_set)}")

#Difference, -
print(f"Difference: {my_set.difference(new_set)}")

#issubset, <=
print(f"issubset: {my_set.issubset(new_set)}")

#Add - adds item to the set
my_set.add("hello")
print(f"Adding an item: {my_set}")

#Remove - removes item from the set
my_set.remove(4.5)
print(f"Removing an item: {my_set}")

#Pop - removes the first element from the set
my_set.pop()
print(f"Pop: {my_set}")

#Pop - removes the first element from the set
my_set.pop()
print(f"Pop: {my_set}")

#Clear - removes all elements from the set
my_set.clear()
print(f"Clear: {my_set}")

#set() is the empty set