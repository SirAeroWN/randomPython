# This program solves Eulers problem 17
# problem 17: If all the numbers from 1 to 1000 inclusive were written out in words, how many letters would be used?
## note: do not count spaces or hyphens, use 'and' in hundreds numbers. For example, 142 is one hundred and forty-two


def wordbuilder(useless):
	# we need to develop a way to convert a number to a word
	## first lets put together some dictionaries

	# ones place name dictionary
	ones = { 0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine' }

	# tens place name dictionary
	tens = { 0:'', 1:'ten', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety' }

	# hundreds place name dictionary (leave out spaces)
	hundreds = { 0:'', 1:'onehundred', 2:'twohundred', 3:'threehundred', 4:'fourhundred', 5:'fivehundred', 6:'sixhundred', 7:'sevenhundred', 8:'eighthundred', 9:'ninehundred' }

	# this gets the basics, but what about the teens?
	# special teens definitions
	teens = { 0:'ten', 1:'eleven', 2:'twelve', 3:'thirteen', 4:'fourteen', 5:'fifteen', 6:'sixteen', 7:'seventeen', 8:'eighteen', 9:'nineteen' }

	# but how do we know when to use the teens instead of the usual system?
	## We'll simply have our code peek ahead when the tens place is a 1

	# now lets get down to the meat
	summ = 0															# accumulator
	for i in range(1, 1001):											# use 1001 because range() is not inclusive on upper limit
		s = str(i)														# convert to a string
		word = ''														# use this to build up word
		teen = False													# a flag to check if number has teens
		if len(s) == 4:													# pad it with leading zeros if nessesary
			#cool
			do = 'nothing'
		elif len(s) == 1:
			s = '000' + s
		elif len(s) == 2:
			s = '00' + s
		elif len(s) == 3:
			s = '0' + s

		# eval thousands place
		if int(s[0]) == 1:
			word = "onethousand"

		# eval hundreds place
		word = word + hundreds[int(s[1])]								# dict lookup

		# need to peek ahead to see if we need to add 'and'
		if int(s[1]) != 0 and (int(s[2]) != 0 or int(s[3]) != 0):		# if the tens or ones place is a non-zero number need the 'and'
			word = word + 'and'

		# eval tens place
		if int(s[2]) == 1:												# dict lookup if possibly a teen
			word = word + teens[int(s[3])]
			teen = True													# set teen flag
		else:
			word = word + tens[int(s[2])]								# dict lookup

		# eval ones place
		if not teen:
			word = word + ones[int(s[3])]								# dict lookup if flag not set

		summ += len(word)												# add length to accumulator

	return summ															# answer: 21124

# sweet! we got what we wanted! but we could make it a little less computationaly intensive
## How? well, we don't actually need to figure out the words! we can instead have the dict values be the number of letters in the word and add that directly to the accumulator
## Let's rewrite the first function to do this instead!
def wordAccumulator(useless):
	# we need to develop a way to convert a number to a word
	## first lets put together some dictionaries

	# ones place name dictionary
	ones = { 0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4 }

	# tens place name dictionary
	tens = { 0:0, 1:3, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6 }

	# hundreds place name dictionary (leave out spaces)
	hundreds = { 0:0, 1:10, 2:10, 3:12, 4:11, 5:11, 6:10, 7:12, 8:12, 9:11 }

	# this gets the basics, but what about the teens?
	# special teens definitions
	teens = { 0:3, 1:6, 2:6, 3:8, 4:8, 5:7, 6:7, 7:9, 8:8, 9:8 }

	# but how do we know when to use the teens instead of the usual system?
	## We'll simply have our code peek ahead when the tens place is a 1

	# now lets get down to the meat
	summ = 0															# accumulator
	for i in range(1, 1001):											# use 1001 because range() is not inclusive on upper limit
		s = str(i)														# convert to a string
		teen = False													# a flag to check if number has teens
		if len(s) == 4:													# pad it with leading zeros if nessesary
			#cool
			do = 'nothing'
		elif len(s) == 1:
			s = '000' + s
		elif len(s) == 2:
			s = '00' + s
		elif len(s) == 3:
			s = '0' + s

		# eval thousands place
		if int(s[0]) == 1:
			summ += 11

		# eval hundreds place
		summ += hundreds[int(s[1])]								# dict lookup

		# need to peek ahead to see if we need to add 'and'
		if int(s[1]) != 0 and (int(s[2]) != 0 or int(s[3]) != 0):		# if the tens or ones place is a non-zero number need the 'and'
			summ += 3

		# eval tens place
		if int(s[2]) == 1:												# dict lookup if possibly a teen
			summ += teens[int(s[3])]
			teen = True													# set teen flag
		else:
			summ += tens[int(s[2])]								# dict lookup

		# eval ones place
		if not teen:
			summ += ones[int(s[3])]								# dict lookup if flag not set

	return summ															# answer: 21124


# lets compare the answers...
#wordbuilder()
#wordAccumulator()

# they're the same! so now let's see if the new program is any faster
## first let's build a timing function
def timeTest(funcs, args, runs):								# takes a list with functions, any arguments as a list, and the number of runs to test over
	import time

	exTimes = [0] * len(funcs)

	for i in range(runs):
		for j in range(len(funcs)):
			for k in range(runs):
				start = time.time()
				funcs[j](args)
				exTimes[j] += time.time() - start

	for i in range(len(exTimes)):
		exTimes[i] = exTimes[i] / (runs * runs)
	return exTimes

# next let's build a way to easily show the times
def displayTimes(funcs, args, runs, timeTester):
	timeList = timeTester(funcs, args, runs)
	for i in range(len(timeList)):
		if i == 0:
			print("Function 1:", timeList[i], "s")
		else:
			print("Function ", i + 1, ": ", timeList[i], " s; ", ((timeList[0] / timeList[i]) * 100) - 100, " % change from ", 1, sep="")

# now to run the test
#displayTimes([wordbuilder, wordAccumulator], 0, 10, timeTest)
