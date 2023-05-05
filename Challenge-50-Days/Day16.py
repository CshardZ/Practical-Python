"""
Challenge #16:

Day 16: Sum the List
Write a function called sum_list with one parameter that takes a nested list of integers as an argument and returns the sum of the integers. 
For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]] as an argument your function should return a sum of 33.


Extra Challenge: Unpack A Nest

Nested_list = [[12, 34, 56, 67], [34, 68, 78]]
Write a code that generates a list of the following numbers from the nested list above  34, 67, 78. Your output should be another list:
[34, 67, 78]. The list output should not have duplicates

"""
# Challenge-16
def sum_list1(llist):
    return sum([j if type(j) != list else sum(j) for i in llist for j in i])

new = []
def sum_list2(llist):
    for i in llist:
        if type(i) == list:
            sum_list2(i)
        else : new.append(i)
    
    return sum(new)

print(sum_list1([[2, 4, 5, 6], [2, 3, 5, 6]])) # 33
print(sum_list2([[2, 4, 5, 6], [2, 3, 5, 6]])) # 33

#Extra
def unpack(llist):
    from itertools import chain
    return list(set(chain(*llist)))

print(unpack([[12, 34, 56, 67], [34, 68, 78]])) # [34, 67, 68, 12, 78, 56]
