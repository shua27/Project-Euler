# Sieve of eratosthenes 

def sieve(limit):
	a = [True] * limit
	a[0] = a[1] = False

	for(i, isprime) in enumerate(a):
		if isprime:
			yield i
			for n in range(i*i, limit, i):
				a[n] = False

sum = 0
for i in sieve(2000000):
	sum += i

print sum
