# Challenge-10
def hide_password(pwd):
    return f"'{len(pwd )*'*'}'"

print(hide_password('hidden')) # '******'

# Extra
nums = [1000000, 2356989, 22354672, 9878098]

def seperator(llist): 🥴
    res = []
    for n in llist:
        nums = []
        for i in str(n):
            nums.append(i)
        for i in range(len(nums)-3,-1,-3):
            nums.insert(i,',')
        
        res.append(''.join(nums))
    return res

print(seperator(nums)) # ['1,000,000', '2,356,989', '2,354,672', '9,878,098']

def seperator2(llist):
    nums = [f"{n:,d}" for n in llist]
    return nums
print(seperator2(nums)) # ['1,000,000', '2,356,989', '22,354,672', '9,878,098']
