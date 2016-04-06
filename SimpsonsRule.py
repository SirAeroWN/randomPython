# simpsons aproximation rule = (dx/3)[f(x0) + 4f(x1) + 2f(x2) + ... + 2f(xN-2) + 4f(xN-1) + f(xN)]
#dx = (b-a)/N

import math

def f(x):
	y = (1 + (math.sin(x) + x*math.cos(x))**2)**0.5
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

switch = True

for i in range(1, len(xs) - 1):
	print("x", xs[i], "f(x)", f(xs[i]))

	if switch:
		total += 4 * f(xs[i])
		switch = False
	else:
		total += 2 * f(xs[i])
		switch = True
	
print("x", xs[-1], "f(x)", f(xs[-1]))


print("Aproximation:", ((dx/3)*total))