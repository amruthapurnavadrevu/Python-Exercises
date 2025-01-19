# Built-in Collection Data Types: Lists

#Repetition is a repetition of references to the data objects in the sequence

my_list = [1,2,3,4]

A = [my_list]*3 #List of lists - all sublists point to the same memory location i.e. they are the same object
B = my_list*3 #Flat list; independent copies

print(f"A={A}")
print(f"B={B}")

my_list[2] = 45

print(f"Original list = {my_list}")
print(f"A={A}")
print(f"B={B}")

#List Methods
#All of them are invoked using the dot notation

new_list = [1024, 3, True, 6.5]

#Append
new_list.append(False)
print(f"Append: {new_list}")

#Insert (index,value)
new_list.insert(2,4.5)
print(f"Insert: {new_list}")

#pop
#Removing and returning the last item from the list
print(f"Pop last item: {new_list.pop()}")
#Removing and returning the item at the index 1
print(f"Pop item at index 1: {new_list.pop(1)}")

#Sort
new_list.sort()
print(f"Sorted list: {new_list}")

#Reverse
new_list.reverse()
print(f"Reversed list: {new_list}")

#Count
print(f"Count the number of occurences of 6.5: {new_list.count(6.5)}")

#Index
print(f"Index of the first occurence of 4.5: {new_list.index(4.5)}")

#Remove
new_list.remove(6.5)
print(f"Removing the first occurrence of 6.5: {new_list}")

#Delete
del new_list[2]
print(f"deleting the item in 2nd position: {new_list}")

#Range

print(list(range(10))) #Starts with 0, not including 10
print(list(range(5,10))) #Starts with 5, not including 10
print(list(range(5,10,2))) #Starts with 5, not including 10, with a step of 2
print(list(range(10,1,-1))) #Starts with 10, not including 1, with a step of -1