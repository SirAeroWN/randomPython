# program for applying simple RSA encryption, destined for use on calculator (TI-nspire)

# wrapper for factoring PQ
def findPQ(PQ):
	t = factor(PQ)
	p = t[0]
	q = t[1]
	return p, q

# guesses x until d is an int according to d = (x(p-1)(q-1) + 1) / e
def findD(p, q, e):
	x = 1
	while not (((x * (p - 1) * (q - 1)) + 1.0) / e) == (((x * (p - 1) * (q - 1)) + 1.0) / e) // 1:
		x += 1
	return (((x * (p - 1) * (q - 1)) + 1.0) / e)

# ecrypts encoded text T according to RSA encrypt method
def encrypt(T, E, P, Q):
	return (T ** E) % (P * Q)

# decrypts encrypted cipher eg opposite of encrypt
#### ^ really earth shattering stuff, huh?
def decrypt(C, D, P, Q):
	return (C ** D) % (P * Q)

# encodes character using simple cipher where a=1, b=2, ..., z=26 with special char ♥=27 and space=28
def encode(c):
	#return ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "♥", " "].index(c) + 1
	return ord(c)

# opposite of encode
#### ^ breaking all the boundries, man
def decode(c):
	#return ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "♥", " "][int(c - 1)]
	return chr(c)

# brute force factoring algorithim, could probably improve speed using list of primes but I'll wait to check performance on calc
def factor(n):
	factors = []
	i = 1
	while i <= n**0.5:
		if n % i == 0:
			if i != 1:
				factors.append(i)
				factors.append(n // i)
		i += 1
	return factors

# test if numbers are co-prime, return true or false
def coprime(a, b):
	afactors = factor(a)
	bfactors = factor(b)
	for f in afactors:
		if f in bfactors:
			return False
	return True

# get p and q from user, if they only have pq, then factor it into p and q
def getPQ():
	p = input("P[blank for PQ]: ")
	if p == "":
		PQ = int(input("PQ: "))
		p, q = findPQ(PQ)
		print("P =", p)
		print("Q =", q)
	else:
		p = int(p)
		q = int(input("Q: "))
	return p, q

# get user text, encode, return as list of cipher encoded text
def getText():
	S = input("message: ").strip()
	C = []

	for c in S:
		C.append(encode(c))
	return C

# get user ciphered text, return properly formatted
def getCiphered():
	S = input("enter cipher text, space delimited: ").strip().split(" ")
	I = []
	for s in S:
		I.append(int(s))
	return I

def getEncrypted():
	S = input("enter encrypted nums, space delimited: ").strip().split(" ")
	I = []
	for s in S:
		I.append(int(s))
	return I

# encrypt and decrypt the message, to make sure d was computed correctly
def eANDd_t(p, q, e, d):
	S = getText()

	C = []
	for c in S:
		print(encrypt(c, e, p, q))			# encode before encrypting
		C.append(encrypt(c, e, p, q))		# append to list to store for decrypting

	for c in C:
		print(decode(decrypt(c, d, p, q)), end="")			# decode after decrypting
	print()

def eANDd_c(p, q, e, d):
	S = getCiphered()

	C = []
	for c in S:
		print(encrypt(c, e, p, q))			# encrypt
		C.append(encrypt(c, e, p, q))		# append to list to store for decrypting

	for c in C:
		print(decrypt(c, d, p, q), end=", ")		# decrypt
	print()

# get p, q, e and compute d
p, q = getPQ()
e = int(input("E: "))
if not coprime(e, (p - 1)*(q - 1)):
	print("E not valid")
d = int(findD(p, q, e))
print("d is =", d)

# find out what user wants to do
mode = input("Enter mode[e,d,b]: ")

if mode == "e":
	# do encrypt stuff
	mode = input("t for text or c for cipher: ")

	if mode == "t":
		# handle text
		text = getText()
		C = []
		for t in text:
			C.append(encrypt(t, e, p, q))
		for c in C:
			print(c, end=", ")

	elif mode == "c":
		# handle cipher
		cipher = getCiphered()
		C = []
		for t in cipher:
			C.append(encrypt(t, e, p, q))
		for c in C:
			print(c, end=", ")

elif mode == "d":
	# do decrypt stuff
	encrypted = getEncrypted()
	C = []
	for t in encrypted:
		C.append(decrypt(t, d, p, q))
	for c in C:
		print(c, end=", ")
	print()
	for c in C:
		print(decode(c), end="")

elif mode == "b":
	# do both
	mode = input("t for text or c for cipher: ")

	if mode == "t":
		# handle text
		eANDd_t(p, q, e, d)

	elif mode == "c":
		# handle cipher
		eANDd_c(p, q, e, d)
print("done")