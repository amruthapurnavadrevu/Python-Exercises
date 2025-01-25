print("hello")

print("Hello","World") #Blank is the default separator

print("Hello","World",sep="***")

print("Hello","World",end="***\n")

print("Hello",end="***");print("World")

#f-strings

height = 156.89
is_tall = True

print(f"Your height is {height} and it is {str(is_tall).lower()} that you are tall.")