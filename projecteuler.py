# =========== Number 1 ============ #
# Sum of all multiples of 3 or 5 below 1000
nums = [num for num in range(1000) if num%3==0 or num%5==0]
print(sum(nums))

# =========== Number 2 ============ #
# Sum of even Fibonacci terms whose values do not exceed 4,000,000
def fibonacci(n):
	if n <= 0:
		return "Enter a valid position"
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

def fib(s):
	seq = []
	for i in range(1, s+1):
		if i == 1:
			seq.append(0)
		elif i == 2:
			seq.append(1)
		else:
			seq.append( fibonacci(i-1) + fibonacci(i-2) )
			if seq[-1] > 4000000:
				break
	return sum([num for num in seq if num%2 == 0])
	# return seq

print(fib(34))


# =========== Number 3 ============ #
# largest prime factor of 600851475143

d = 3
n = 600851475143
primes = []

while d ** 2 < n:
    if n % d == 0:
        n /= d
        primes.append(d)
    else:
        d += 2
        
# last value of n is the largest prime factor
primes.append(n)
# view all primes factors
print(primes)
# view largest prime factor 	
print(max(primes))

