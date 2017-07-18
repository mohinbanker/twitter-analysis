import math


def f():
	a = 1
	c = 0
	while a < 500:
		b = a
		while b < 500:
			c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
			if (a + b + c) == 1000:
				print([a,b,c])
				print(a * b * c)
				return
			if (a + b + c) > 1000:
				break
			b += 1
		a += 1

f()
