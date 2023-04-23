"""
Challenge #14:
Day 14: Flatten the List
Write a function called flat_list that takes one argument, a nested list. 
The function converts the nested list into a one- dimension list. For example [[2,4,5,6]] should return [2,4,5,6].

Extra Challenge: Teacher’s Salary
A school asked you to calculate teachers' salaries. 
The program should ask the user to enter the teacher’s name, the number of periods taught in a month, and the rate per period.
The monthly salary is calculated by multiplying the number of periods by the monthly rate. The current monthly rate per period is $20.
If a teacher has more than 100 periods in a month, everything above 100 is overtime. 
Overtime is $25 per period. For example, if a teacher has taught 105 periods, their monthly gross salary should be 2,125. 
Write a function called your_salary that calculates a teacher’s gross salary.
The function should return the teacher’s name, periods taught, and gross salary. Here is how you should format your output:
Teacher: John Kelly, Periods: 105
Gross salary:2,125
"""

def flat_list(llist):
    new_list = []
    for i in llist:
        new_list.extend(i)
    return new_list
print(flat_list([[2,4,5,6],[4,5]])) #[2, 4, 5, 6, 4, 5]

def your_salary():
    name = input("Enter teacher's name: ")
    periods = int(input("Total period taken in month: "))
    if periods<=100:
        sal = 100*20
    else:
        overtime = periods - 100
        sal = (100*20) + (overtime*25)
    return f"""
    Teacher: {name}, Periods: {periods}
    Gross salary:${sal}"""

print(your_salary())
"""
Enter teacher's name: JeffGates
Total period taken in month: 105

    Teacher: JeffGates, Periods: 105
    Gross salary:$2125
"""
