
####################
### NOT FINISHED ###
####################

def simplify(number):
	global inside
	inside = number
	out = simplifyHelper(number, 2)
	if inside == 1:
		stringForm = str(out)
	else:
		stringForm = str(out) + 'sqrt(' + str(inside) + ')'
	return stringForm

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

simplifying = True

while simplifying:
	print(simplify(eval(input('Enter a number: '))))