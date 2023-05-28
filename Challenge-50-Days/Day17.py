"""
Challenge #17:

Day 17: User Name Generator

Write a function called user_name, that creates a username for the user. The function should ask a user to input their name.
The function should then reverse the name and attach a randomly issued number between 0 – 9 at the end of the name.
The function should return the username.


Extra Challenge: Sort by Length

names = [ "Peter", "Jon", "Andrew"]
Write a function called sort_length that takes a list of strings as an argument, and sorts the strings in ascending order according to their length. 
For example, the list above should return:
['Jon', 'Peter', 'Andrew']
Do not use the built-in sort functions
"""

def user_name():
    from random import randint
    name = input("Enter your name: ")
    return name[::-1] + str(randint(0,9))

print(user_name()) # setaGffeJ6


def sort_length(names):
    #return sorted(sorted(names), key=len)
    sorted_names = sorted(names)
    return sorted(sorted_names, key=len)

print(sort_length([ "Peter", "Jon", "Andrew"])) # ['Jon', 'Peter', 'Andrew']

