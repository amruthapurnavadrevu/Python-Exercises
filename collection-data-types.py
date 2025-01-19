# Built-in Collection Data Types

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
