#This is a program to find symbolic derivatives of user input

class Term():
	def __init__(self, constant, exponent = 0):
		self.exp = exponent
		self.con = constant
		return

class Poly():
	def __init__(self, terms = []):
		self.terms = terms
		return

	def __str__(self):
		return self.terms

	def addTerm(self, newTerm):
		self.terms.append(newTerm)
		return

def prompt():
	userIn = input('please enter a polynomial for derivation: ')
	return terminate(userIn)

def terminate(expression):
	LePoly = Poly()
	cont = True
	indivTerm = expression[0]
	i = 1
	while cont:
		print('terminate1')
		if i < len(expression):
			if expression[i] != '-' and expression[i] != '+':
				indivTerm += expression[i]
			else:
				cont = False
			i += 1
		else:
			cont = False
	LePoly.addTerm(analyze(indivTerm))
	while i < len(expression):
		print('terminate2', i)
		cont = True
		while cont:
			print('terminate3')
			if i < len(expression):
				if expression[i] != '-' and expression[i] != '+':
					indivTerm += expression[i]
				else:
					cont = False
				i += 1
			else:
				cont = False
			LePoly.addTerm(analyze(indivTerm))
	return LePoly

def analyze(strTerm):
	if strTerm[0] == '+':
		i = 1
	else:
		i = 0
	const = ''
	expo = ''
	control = True
	if i < len(strTerm):
		while control:
			print('analyze1')
			if i < len(strTerm):
				if strTerm[i] != 'x':
					const += strTerm[i]
				else:
					const = float(const)
					control = False
			else:
				control = False
			i += 1
	if i < len(strTerm):
		if strTerm[i] == '^':
			i += 1
			control2 = True
			while control2:
				print('analyze2')
				if i < len(strTerm):
					expo += strTerm[i]
				else:
					expo = float(expo)
					control2 = False
				i += 1
			return Term(const, expo)
	return Term(const)

print(prompt())