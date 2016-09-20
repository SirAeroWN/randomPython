# trapezoidal aproximation rule = (dx/2)[f(x0) + 2f(x1) + ... + 2f(xN-1) + f(xN)]
#dx = (b-a)/N

import math

def f(x):
	y = 8 * math.cos((x**2))
	return y

a = float(input("a: "))
b = float(input("b: "))
N = float(input("N: "))
dx = (b - a) / N

xs = []
i = a
while i <= b:
	xs.append(i)
	i += dx

total = f(xs[0]) + f(xs[-1])

print("x", xs[0], "f(x)", f(xs[0]))

for i in range(1, len(xs) - 1):
	print("x", xs[i], "f(x)", f(xs[i]))

	total += 2 * f(xs[i])
	
print("x", xs[-1], "f(x)", f(xs[-1]))


print("Aproximation:", ((dx/2)*total))