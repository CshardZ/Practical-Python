def only_floats(a,b):
	if isinstance(a, float) and isinstance(b, float):
		return 2
	elif isinstance(a,float) or isinstance(b, float):
		return 1
	else:
		return 0

print(only_floats(23,2.001)) # 1
print(only_floats(23.2,23.24)) # 2
print(only_floats(2,2)) # 0



# Extra
def word_index(w_list): # RIDICULOUS😑
	max_list = ['']
	larg = 0
	for ind,word in enumerate(w_list):
		
		if len(word) > larg:
			larg = len(word)
			max_list.pop()
			max_list.append(ind)
		
		elif len(word) == larg:
			max_list.append(ind)
		
					
	if len(max_list) == len(w_list):
		return 0
	
	return f"At index {max_list}"

words1 = ["Hate", "remorse", "vengeance", "vengeance"]
words2 = ['aaa','aaa','aaa','aaa']

print(word_index(words1)) # At index [2,3]
print(word_index(words2)) # 0
