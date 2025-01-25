#2 Purposes: Iteration and Selection

#Iteration

#while; for

n=0
while n<5:
    print(f"The n value is {n}")
    n+=1

word_list = ['apple','bear','cotton']
letter_list = []
for word in word_list:
    for letter in word:
        if letter not in letter_list:
            letter_list+=letter

print(letter_list)

#Selection 

#if, ifelse

score = 70 
if score>=90 and score<100:
    print("Grade is A")
elif score>=80 and score<90:
    print("Grade is B")
elif score>=70 and score<80:
    print("Grade is C")
elif score<70:
    print("Try again")

#List Comprehension
#for creating a list that uses iteration and selection constructs
#it allows you to create a list based on some processing or selection criteria

#List of first 10 squares
list_new = []
for i in range(1,11):
    list_new.append(i**2)
print(list_new)

#using list comprehension
list_comp = [i**2 for i in range(1,11)]
print(list_comp)

#adding selection to list
list_comp_2 = [i*i for i in range(1,11) if i%2==0]
print(list_comp_2)

#Redoing characters in words in a list
words = ['cat','dog','rabbit']
list_comp_letters = list({letter for word in words for letter in word})
print(list_comp_letters)

