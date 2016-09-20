# This program solves Eulers problem 17
# problem 17: sum all the digits of 2^1000

# The simplest way to do this is to just compute 2^1000 and then sum the digits:
def methodOne():
	num = 2 ** 1000				# calculate 2^1000
	stringNum = str(num)		# convert to string
	summ = 0					# this is the running sum variable. Using 'summ' because 'sum' is a reserved word
	for c in stringNum:
		summ += int(c)			# iterate through  all the characters, convert to ints and add to running total
	print(summ)

# That was easy because Python can handle big numbers, but if we were using a different language we would have to adapt,
## so lets do it the fun way
def methodTwo():
	digits = [0] * 400							# there are 300 digits in 2^1000, using 400 Just In Case (tm)
	digits[0] = 1								# set the first digit to 1 because we are iterating **power** times which includes the first 2
	carry = 0									# need a carry var since we are essentially doing long multiplication
	for i in range(1000):						# iterate **power** number of times
		for d in range(len(digits)):			# go through all digits in in array
			carry = (2*digits[d]) + carry		# multiply by base and add previous carry, storing in 'carry' because I can, could easily use another variable
			digits[d] = carry % 10				# previous sum mod 10 gives what the new value for the digit is
			carry = carry // 10					# previous sum integer divide 10 gives new carry value, either 0 or 1
	#print(digits)
	summ = 0
	for d in digits:							# sum all digits
		summ += d
	print(summ)									# now wasn't that so much more fun? Runs slower but who cares?


methodOne()
methodTwo()