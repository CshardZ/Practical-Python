# Challenge-10
def hide_password(pwd):
    return f"'{len(pwd )*'*'}'"

hide_password('hide')

# Extra
def seperator(llist):
    res = []
    for n in llist:
        num = str(n)
        nums = []
        for i in num:
            nums.append(i)
        for i in range(len(nums)-3,-1,-3):
            nums.insert(i,',')
        
        res.append(''.join(nums))
    
    return res

nums = [1000000, 2356989, 22354672, 9878098]
print(seperator(nums)) # ['1,000,000', '2,356,989', '2,354,672', '9,878,098']
