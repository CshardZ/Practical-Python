# Challenge -09
def biggest_odd(string):
    return max([n for n in string if int(n) % 2 != 0])

print(biggest_odd('342789')) # 9

# Extra
def zero_last(llist):
    for i in range(len(llist)):
        if 0 in llist:
            llist.remove(0)
            llist.append(0)
    return llist.sort()
print(zero_last([2,4,7,2,6,0,1,0,0,4,5,0])) # [1, 2, 2, 4, 4, 5, 6, 7, 0, 0, 0, 0]
