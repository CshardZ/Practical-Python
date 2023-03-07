# Challenge-08
def odd_even(nums):
	return max([n for n in nums if n % 2 == 0]) - min([n for n in nums if n % 2 != 0])

nums = [5,8,9,10,22]
print(odd_even(nums)) # 17

# Extra
def primes(rng):
	primes = []
	for n in range(2,rng):
		for f in range(2,n):
			if n%f == 0:
				break
		else:
			primes.append(n)
	return primes

print(primes(20)) #[2, 3, 5, 7, 11, 13, 17, 19]
