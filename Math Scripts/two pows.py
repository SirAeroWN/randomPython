a = 0
for i in range(3, 10):
	print(2**i, (1.0 / 2**i))
	a += (1.0 / 2**i)
print(a)