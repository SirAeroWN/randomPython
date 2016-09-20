# midpoint aproximation rule = dx[f(x0) + 2f(x1) + ... + 2f(xN-1) + f(xN)] where xN = (1/2)(xN-1 + xN)
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

total = 0

for i in range(1, len(xs)):
	xAVG = (1 / 2) * (xs[i - 1] + xs[i])
	total += f(xAVG)

	print("x{0}: {1}".format(i -1, xs[i - 1]), "x{0}: {1}".format(i, xs[i]), "average: {0}".format(xAVG), "xAVG^2: {0}".format(xAVG**2), "f(xAVG): {0}".format(f(xAVG)))

print("Aproximation:", (dx*total))