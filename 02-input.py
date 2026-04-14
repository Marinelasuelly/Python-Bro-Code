# input() = A function that prompts the user to enter data 
#    Returns the entered data as a string

name=input("What is your name?\nA: ")
age = input("How old are you?\nA: ") # it accept the output of the user as an string 

age  = int(age) # it converts to an integer because 
age = age + 1 #we cannot concatenate string with integer
print(f"Hello {name}!")
print("HAPPY BIRTHDAY!!!\n")
print(f"Wow! You are {age} now.")