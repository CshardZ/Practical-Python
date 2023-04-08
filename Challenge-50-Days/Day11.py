#  Challenge-11

def equal_strings(str1,str2):
    return sorted(str1) == sorted(str2)        

print(equal_strings('love','evol')) # True

# Extra
def swap_values(llist):
    llist[0],llist[-1] = llist[-1],llist[0]
    return llist

print(swap_values([2,4,7,8])) # [8,4,7,2]
