# finds roots

def get(letter):
	string = letter + ' = '
	imp = input(string)
	while len(imp) == 0:
		imp = input('YOU DIDN\'T ENTER A NUMBER!!!!! try again: ' + letter + ' = ')
	if imp != 'q':
		imp = eval(imp)
	return imp

print("Equations are of the form ax^2 + bx + c\n'j's are used to stand for 'i's\nYou may type 'q' at any prompt to quit")

def pureNum():
	doinProbs = True

	while doinProbs:
		a = get('a')
		if a == 'q':
			print('Goodbye')
			break
		b = get('b')
		if b == 'q':
			print('Goodbye')
			break
		c = get('c')
		if c == 'q':
			print('Goodbye')
			break

		descriminant = b**2 - (4 * a * c)

		x1 = ((-1 * b) + (descriminant**0.5)) / 2*a
		x2 = ((-1 * b) - (descriminant**0.5)) / 2*a

		print('x = ', end = '')
		print(x1, end = '')
		print(', ', end = '')
		print(x2)
	return

def retrieve():
	string = 'Enter an equation in the form ax^2+bx+c: '
	imp = input(string)
	while len(imp) == 0:
		imp = input('YOU DIDN\'T ENTER ANYTHING!!!!! try again: ')
	return imp.strip()

def getsign(equation, position):
	sign = equation[position]
	if sign == '-':
		return -1, position +1
	else:
		return 1, position +1

def parse(imp):
	place = 0
	a, place = getNum(imp, place)
	place += 3
	bSign, place = getsign(imp, place)
	b, place = getNum(imp, place)
	b = b * bSign
	place += 1
	c, place = getNum(imp, place)
	return a, b, c

def getNum(equationString, position):
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	strNum = ''
	if equationString[position].lower() in letters:
		return 1, (position)
	while equationString[position].lower() not in letters:
		strNum += equationString[position]
		position += 1
		if position == len(equationString):
			break
	return eval(strNum), position

def simplify(number):
	global inside
	inside = number
	listReturn = [1,'r',1]
	if inside == 0:
		return [0, 'r', 0]
	elif inside < 0:
		listReturn[1] = 'i'
		inside = inside * -1
		number = number * -1
	out = simplifyHelper(number, 2)
	listReturn[0] = out
	listReturn[2] = inside
	return listReturn

def simplifyHelper(number, devisor):
	if devisor > 50:
		global inside
		inside = number
		return 1
	outside = 1
	if (number % devisor**2) == 0:
		outside = devisor
		number = number // devisor**2
		return outside * simplifyHelper(number, devisor)
	else:
		return outside * simplifyHelper(number, devisor + 1)

def reduction(bTerm, discriminant, denominator):
	for i in range(denominator, 1, -1):
		if (bTerm % i == 0) and (discriminant[0] % i == 0) and (denominator % i == 0):
			bTerm = bTerm // i
			discriminant[0] = discriminant[0] // i
			denominator = denominator // i
	return bTerm, discriminant, denominator

def stringify(info):
	bTerm = info[0]
	disc = info[1]
	denom = info[2]
	first = str(bTerm)
	second = discString(disc)
	if denom != 1:
		third = '\n' + '-' * len(first + second + ' + ') + '\n'
		fourth = ' ' * (len(first + second + ' + ') // 2) + str(denom)
		back = second + third + fourth
	else:
		back = second
	if second == '':
		x = first + back
	else:
		x = first + ' ' + "\u00B1" + ' ' + back
	return x

def discString(discList):
	if discList[0] == 0 or discList[2] == 0:
		return ''
	string = ''
	if discList[0] == 1:
		string += ''
	else:
		string += str(discList[0])
	if discList[1] == 'i':
		string += 'i'
	if discList[2] == 1 and discList[0]  == 1:
		string += '1'
	elif discList[2] == 1 and discList[0] != 1:
		string += ''
	else:
		string += 'sqrt(' + str(discList[2]) + ')'
	return string
	
def symbolic():
	working = True

	while working:
		equation = retrieve()
		if equation == 'q':
			break
		a, b, c = parse(equation)
		desc = simplify(b**2 - (4 * a * c))
		first = -1 * b
		den = 2 * a
		final = stringify(reduction(first, desc, den))
		print(final, end = '\n\n')
	return

symbolic()