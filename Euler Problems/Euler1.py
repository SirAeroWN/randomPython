# This program solves Eulers problem 1
## problem 1: What is the sum of all the multiples of 3 and or 5 under 1000

# Ok, so this is essentially a fizzbuzz problem and should be pretty straight forward
acc = 0								# our accumulator

for i in range(1, 1000):			# loop through every number under 1000, inclusive
	if i % 3 == 0 or i % 5 == 0:	# if divisible by 3 or 5 then mod = 0
		acc += i 					# add to accumulator

print(acc)							# display answer