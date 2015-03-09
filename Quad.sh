function retrieve {
	echo "Enter an equation in the form ax^2+bx+c: "
	read imp
	return imp
}

function getsign(equation, position):
	sign = equation[position]
	if sign == '-':
		return -1, position +1
	else:
		return 1, position +1

function parse(imp):
	place = 0
	a, place = getNum(imp, place)
	place += 3
	bSign, place = getsign(imp, place)
	b, place = getNum(imp, place)
	b = b * bSign
	place += 1
	c, place = getNum(imp, place)
	return a, b, c

function getNum(equationString, position):
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

function simplify(number):
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

function simplifyHelper(number, devisor):
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

function reduction(bTerm, discriminant, denominator):
	for i in range(denominator, 1, -1):
		if (bTerm % i == 0) and (discriminant[0] % i == 0) and (denominator % i == 0):
			bTerm = bTerm // i
			discriminant[0] = discriminant[0] // i
			denominator = denominator //i
	return bTerm, discriminant, denominator

function stringify(info):
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

function discString(discList):
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
	
function symbolic():
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