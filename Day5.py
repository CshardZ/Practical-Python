# Challenge -05

def my_discount():
	
	price = float(input("Enter price: "))
	disc = float(input("Enter discount(%): "))
  f_price = price - (price*disc/100)
	return f"Final pricee: {f_price}"

print(my_discount())

# Extra
students = ['Male', 'Female', 'female', 'male', 'male', 'male','female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

def sex_count(llist):
	males = 0
	females = 0
	others = 0
	for i in llist:
		i = i.lower()
		if i == 'male':
			males += 1
		elif i == 'female':
			females += 1
		else:
			others += 1
    
    return [('Male',males),('Female',females),('Other',others)]

print(sex_count(students))
