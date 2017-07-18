import math

def primes(upperBound):
	# Returns list of all primes below upperBound
	p = [2, 3]
	i = 4
	while i < upperBound:
		if ((i - 1) % 6 != 0) and ((i + 1) % 6 != 0): # if it doesn't take form 6k +/- 1, not a prime
			i += 1
			continue
		for prime in p:
			if i % prime == 0: # if divisible by prime
				break
			if prime > math.sqrt(i):
				p.append(i)
				break
		i += 1
	return p


p = primes(2000000)
print(sum(p))
