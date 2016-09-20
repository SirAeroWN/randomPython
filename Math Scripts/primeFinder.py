def getPrimes(a):
	def isPrime(p):
		n = 2
		while n < p:
			if p % n == 0:
				return False
			n += 1
		return True

	prime = 2
	primes = []

	while prime < a[0]:
		if isPrime(prime):
			#print(prime, end=", ")
			primes.append(prime)
		prime += 1

def getSquares():
	s = 1
	while s < 100:
		print(s**2, end=", ")
		s+=1

def getPrimes2(a):
	primes = [2]
	n = 3
	while n < a[0]:
		if not dividedBy(n, primes):
			primes.append(n)
		n += 1
	return primes

def dividedBy(num, divisors):
	for i in range(len(divisors)):
		if divisors[i] > (num / 2):
			break
		elif num % divisors[i] == 0:
			return True
	return False

def dividedBy2(num, square, divisors):
	for i in range(len(divisors)):
		if divisors[i] > square:
			return False
		elif num % divisors[i] == 0:
			return True

def getPrimes3(a):
	primes = [2, 3, 5]
	n = 6
	while n < a[0]:
		square = n**0.5
		if not dividedBy2(n, square, primes):
			primes.append(n)
		n += 1
	return primes

def getPrimes4(a):
	primes = [2, 3, 5]
	n = 6
	while n < a[0]:
		if int(str(n)[-1]) not in [1, 3, 7, 9]:
			n += 1
			continue
		square = n**0.5
		if not dividedBy2(n, square, primes):
			primes.append(n)
		n += 1
	return primes

def getPrimes4_1(a):
	primes = [2, 3, 5]
	n = 6
	while n < a[0]:
		if n % 10 not in [1, 3, 7, 9]:
			n += 1
			continue
		square = n**0.5
		if not dividedBy2(n, square, primes):
			primes.append(n)
		n += 1
	return primes

def getPrimes5(a):
    potsOld = []
    potsNew = []
    ceiling = a[0]**0.5
    curPrime = 2
    index = 0

    for i in range(2, a[0]):
        potsNew.append(i)

    while curPrime < ceiling:
        potsOld = potsNew
        potsNew = []
        for pos in potsOld:
            if pos < curPrime or pos == curPrime or pos % curPrime != 0:
                potsNew.append(pos)
        index += 1
        curPrime = potsNew[index]
    return potsNew

def getPrimes6(a):
    potsOld = []
    potsNew = [2, 3, 5]
    ceiling = a[0]**0.5
    curPrime = 2
    index = 0

    for i in range(6, a[0]):
        if (i % 10) in [1, 3, 7, 9]:
            potsNew.append(i)

    while curPrime < ceiling:
        potsOld = potsNew
        potsNew = []
        for pos in potsOld:
            if pos < curPrime or pos == curPrime or pos % curPrime != 0:
                potsNew.append(pos)
        index += 1
        curPrime = potsNew[index]
    return potsNew

#########################
###### EXPLENATION ######
#########################
# This is known as a sieve.
# the way it works is you assemble a list of all the numbers under x
# then starting with the first prime number (2) remove all numbers divisible by it (2)
# the next highest number on this list will be the next prime number
# repeat the process with this next number
# again the next highest number will be the next prime
# repeat until the next prime is greater than sqrt(X)
# the list now only contains prime numbers

def getPrimes6_1(a):
    potsOld = []
    potsNew = [2, 3, 5]											# start off with primes 2, 3, 5 because 2 and 5 break the "primes only end in 1, 3, 7, or 9" rule;; include 3 because order is important
    ceiling = a[0]**0.5											# only need to go to the sqrt() of the max prime because any numbers bigger than sqrt() will have to be multiplied by something smaller than sqrt() which are all already prime
    curPrime = 2												# start with first prime
    index = 0

    for i in range(6, a[0]):
        if (i % 10) in [1, 3, 7, 9]:							# eliminate any numbers not follwing prime rule, reduces computaions in next step
            potsNew.append(i)

    while curPrime < ceiling:
        potsOld = potsNew										# transfer the reduced list to the list of possibles
        potsNew = []
        for pos in potsOld:
            if pos <= curPrime or pos % curPrime != 0:			# if the number is smaller than curPrime it has already been vetted as a prime, if it is divisible by curPrime then it isn't included
                potsNew.append(pos)
        index += 1
        curPrime = potsNew[index]								# move to the next highest number in potsNew, it will be a prime
    return potsNew

def timeTest():
	import time

	s = 0

	for t in range(10):
		start = time.time()
		getPrimes3()
		s += time.time() - start
	print(s / 10)
	t1 = s / 10

	s = 0

	for t in range(10):
		start = time.time()
		getPrimes4()
		s += time.time() - start
	print(s / 10)
	t2 = s / 10

	print(((t1 / t2) * 100) - 100, "% more efficient")


def timeTest2(foo, goo, args, times):
	import time

	inc = 0
	fooTime = 0
	gooTime = 0

	for i in range(times):

		for t in range(times):
			start = time.time()
			foo()
			fooTime += time.time() - start

		for t in range(times):
			start = time.time()
			goo()
			gooTime += time.time() - start

	fooTime = fooTime / (times * times)
	gooTime = gooTime / (times * times)

	print("first function time is", fooTime, "seconds")
	print("second function time is", gooTime, "seconds")
	print("\nsecond function is", ((fooTime / gooTime) * 100) - 100, "%   more efficient then the first")


def timeTest3(funcs, args, times):
	import time

	exTimes = [0] * len(funcs)

	for i in range(times):
		for j in range(len(funcs)):
			for k in range(times):
				start = time.time()
				funcs[j](args)
				exTimes[j] += time.time() - start

	for i in range(len(exTimes)):
		exTimes[i] = exTimes[i] / (times * times)
	return exTimes


def displayTimes(funcs, args, times, timeTester):
	timeList = timeTester(funcs, args, times)
	for i in range(len(timeList)):
		if i == 0:
			print("Function 1:", timeList[i], "s")
		else:
			print("Function ", i + 1, ": ", timeList[i], " s; ", ((timeList[0] / timeList[i]) * 100) - 100, " % change from ", 1, sep="")

def testPrimes(a, b):
	if a([100000]) == b([100000]):
		print("It worked!!!")
	else:
		print("Damn it")
#print(getPrimes5([100000]))
#testPrimes(getPrimes4, getPrimes5)
#displayTimes([getPrimes, getPrimes2, getPrimes3, getPrimes4], [100000], 10, timeTest3)
#displayTimes([getPrimes4, getPrimes6], [100000], 10, timeTest3)
primes = getPrimes6([100000])
for p in primes:
	if (p + 2) in primes and (p + 4) in primes and p != 3:
		print(p, p + 2, p + 4)
