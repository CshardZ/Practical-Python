#Challenge -02
def convert_add(str_num_list):
	return sum([int(num) for num in str_num_list])

llist =  ['1','3', '5']
print(convert_add(llist))

# Extra
def check_duplicates(llist):
	from collections import Counter
	temp = Counter(fruits)
	print(set([fruit for fruit in fruits if temp[fruit]>1 ]))

fruits = ['apple', 'orange', 'bannana', 'apple','bannana','cake','cake','ice']
check_duplicates(fruits)
