# This program solves Eulers problem 3
# What is the largest prime factor for the number 600851475143

# this requires finding some primes, which I've done some work in previously:
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


# but this just finds all primes under a certain ceiling, I want the largest prime factor

bigNum = 600851475143

#candidates = getPrimes6_1([bigNum])

best = 0
# for pos in candidates:
# 	if pos % bigNum == 0 and pos > best:
# 		best = pos

#print(best)

# computing all primes under 600 billion takes too long
## this next method takes out the smallest factor, the last indivisible number is the largest prime

def smallestPrime(n):
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return i
	return n

prime = smallestPrime(bigNum)
while prime != bigNum:
	bigNum = bigNum / prime
	prime = smallestPrime(bigNum)

print(int(bigNum))