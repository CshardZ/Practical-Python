# Challenge-07
def string_range(num):
	print('.'.join([str(num) for num in range(num)])+'.')

string_range(10) # 0.1.2.3.4.5.6.7.8.9.10.

# Extra
def dict_names(names):
	name_dict = dict()
	for name in names:
	    if name.upper().startswith('S'):
	        if name in name_dict:
	            name_dict[name] += 1
	        else:
	            name_dict[name] = 1
	return name_dict   

names = ["Joseph","Nathan", "Sasha", "Kelly","Seena", "Jabulani", "Sera", "Patel", "Sera",'Seena','Seena']         
print(dict_names(names)) # {'Sasha': 1, 'Seena': 3, 'Sera': 2}
