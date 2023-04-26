"""
Challenge #15:

Day 15: Same in Reverse
Write a function called same_in_reverse that takes a string and checks if the string reads the same in reverse.
If it is the same, the code should return True.
If not, it should return False.
For example, 'dad' should return True, because it reads the same in reverse.


Extra Challenge: What's My Age?

Write a function called your_age. This function should take a name and then it return their age.
For example, if 'Peter' is passed, your function should return, 'Hi, Peter, you are 27 years old.
This function reads data from the 'database' (dictionary below). 
If the name is not in the dictionary, your code should tell the user that their name is not in the dictionary, and ask them for their age.
Your code should then add the name and age to the dictionary of names_age below. 
Once added your code should return to the user 'Hi, (added name), you are (added age) years old'. Only lowercase names should be stored.

names_age = {"jane": 23, "kerry": 45, "tim": 34, “peter": 27}
"""
# Challenge-15
def palindrome(string):
    return string[0:].lower() == string[::-1].lower()

print(palindrome('Ana')) # True

# Extra
def your_age(name):
    names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}
    if name  not in names_age:
        age = int(input("We cant find that name in database.\nIf you want register please enter your age : "))
        names_age.setdefault(name.lower(), age)
        
    return f"Hi {name}, you are {names_age[name.lower()]} years old."

print(your_age('jane')) #Hi jane, you are 23 years old.     
print(your_age("JeffGates")) # We cant find that name in database.
                             # If you want register please enter your age : 55
                             # Hi JeffGates, you are 55 years old.
