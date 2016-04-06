# for making truth tables, want to develop this a little more after the homework is done

## TODO: implement an entry system for typing logic expressions

def xor(p,q):
	if ((p or q) and not (p and q)):
		return True
	else:
		return False

def NAND(p, q):
	if not (p and q):
		return True
	else:
		return False

def NOR(p, q):
	if not (p or q):
		return True
	else:
		return False

def implies(p,q):
	if ((not p) or q):
		return True
	else:
		return False

def differance(A, B):
	if (A and not B):
		return True
	else:
		return False

def custom1(p, q):
	if ((not (p and q)) and ((not p) and (not q))):
		return True
	else:
		return False

def custom2(p, q, r):
	if (((p or q) or (p or r)) and ((p or q) and r)):
		return True
	else:
		return False

def custom3(p, q):
	if ((not (p or q)) and ((not p) and (not q))):
		return True
	else:
		return False

def custom4(p, q):
	if ((not p) or q):
		return True
	else:
		return False

def custom5(p, q):
	if implies((p and (not q)), False):
		return True
	else:
		return False

def combos(var, count):
	combo = ["T"] * var

	while True:
		for symbol in combo:
			print("| {} ".format(symbol), end="")

		for result in unconvert(test(convert(combo))):
			print("| {} ".format(result), end="")
		print("|")

		combo = iterate(combo, (len(combo) - 1))
		count += 1

		if count > 2**var:
			return

def iterate(counter, index):
	if counter[index] == "T":
		counter[index] = "F"
	else:
		counter[index] = "T"
		if index - 1 < 0:
			return counter
		iterate(counter, index - 1)
	return counter

def convert(abrev):
	theCombo = []
	for val in abrev:
		if val == "T":
			theCombo.append(True)
		else:
			theCombo.append(False)
	return theCombo

def unconvert(elong):
	theCombo = []
	for val in elong:
		if val:
			theCombo.append("T")
		else:
			theCombo.append("F")
	return theCombo

def test(stuff):
	return [custom5(stuff[0], stuff[1])]

# print(" p | q | r | ¬(p^q) and ¬p^¬q | (pVq)V(pVr) and (pVq)^r | ¬(pVq) and ¬p^¬q")
print("| p | q | p -> q | (p ^ ~q) -> F")

count = 1
combos(2, count)