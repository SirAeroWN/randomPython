def factor(n):
	factors = []
	for i in range(1, n + 1):
		if n % i == 0:
			factors.append(i)
	return factors


def factorBetter(n):
	factors = []
	i = 1
	while i <= n**0.5:
		if n % i == 0:
			factors.append(i)
			factors.append(n // i)
		i += 1
	return factors


def timeTest(n):
	import time

	s = 0

	for t in range(10):
		start = time.time()
		factor(n)
		s += time.time() - start
	print(s / 10)

	s = 0

	for t in range(10):
		start = time.time()
		factorBetter(n)
		s += time.time() - start
	print(s / 10)

# timeTest(2154165)
print(factorBetter(int(input("Enter: "))))
