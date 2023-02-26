#Challenge -03

register = {'Michael' : 'yes', 'John' : 'no' , 'Peter' : 'Yes', 'Mary': 'Yes'}

#Normal
def register_check(reg_dict):
	count = 0
	for val in reg_dict.values():
		if val.lower() == 'yes':
			count += 1
	print(f"{count} students.")

register_check(register)

# List-comprehension`
def register_check2(reg_dict):
	count = 1
	print(sum([count for val in reg_dict.values() if val.lower() == 'yes']),'students.')

register_check2(register)


#Extra
names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]

def sorted_names(names):
	names = (sorted(names, key=str.lower))[::-1]
	print(tuple(name for name in names if name.islower())) #🤖

sorted_names(names)
