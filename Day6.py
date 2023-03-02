# Challenge-06
def user_name(user_email):
	name = ''
	for l in user_email:
		if l != '@':
			name += l
		else:
			break
	return name

print(user_name('JeffGates@micromazon.com')) # JeffGates

# Extra
def zeroed_ends(num_list):
	num_list[0] = 0
	num_list[-1] = 0
	return num_list

nums = [2,3,4,5,6,7]
print(zeroed_ends(nums)) # [0, 3, 4, 5, 6, 0]
