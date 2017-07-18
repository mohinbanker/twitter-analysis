from collections import defaultdict
s = 0

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

i = 1
while 1:
	s += i
	p = primes(s)
	factors = defaultdict(lambda: 0)
	for prime in p:
		factors[prime] += 1
	prod = 1
	for key,value in factors.items():
		prod *= (value + 1)
	if prod > 500:
		print(s, prod)
		break
	i += 1