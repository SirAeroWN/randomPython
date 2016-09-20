# This program solves Eulers problem 4
## problem 4: find the largest palindrome made from the product of two 3-digit numbers

best = 0
for i in range(100, 1000):							# go from 100 to 999 inclusive
	for j in range(100, 1000):
		p = i * j
		if str(p) == str(p)[::-1] and p > best:		# p[::-1] inverts a string
			best = i * j

print(best)