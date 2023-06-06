"""
Challenge #18:

Day 18: Any Number of Arguments

Write a function called any_number that can receive any number of arguments (integers and floats) and return the average of those integers.
If you pass 12, 90, 12, 34 as arguments your function should return 37.0 as average. 
If you pass 12, 90 your function should return 51.0 as average.


Extra Challenge: Add and Reverse

Write a function called add_reverse. This function takes two lists as argument and adds each corresponding number, 
and reverses the outcome. For example, if you pass [10, 12, 34] and [12, 56, 78]. Your code should return [112, 22, 68]. 
If the two lists are not of equal lengths, the code should return a message that "the lists are not of equal lengths".
"""


def any_number(*args):
    return sum(args) / len(args)

print(any_number(12, 90, 12, 34)) # 37.0


# Extra

def add_reverse(llist1, llist2): # Works fine🥴
    return [ int(str(llist1[i]+llist2[i])[::-1]) for i in range(len(llist1)) ]

print(add_reverse([10, 12, 34],[12, 56, 78])) # [22, 86, 211]
