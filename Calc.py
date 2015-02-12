from ListStructures import Queue # Stack is memory structure used
from tkinter import * # Using tkinter for GUI

class calc(Queue): # super class is stack so I don't have to make a stack object and call self.name.stackmethod() but can call self.stackmethod()
	def __init__(self):
		super().__init__() # initialize superclass
		self.displayVal = '' # this is the value in the display
		self.number = ''
		self.parenthisis = 0 # number of parenthisis
		self.memory = '0' # number in memory, string so self.display can be easily changed
		root = Tk() # the window
		root.title("RPN") # window title
		#img = PhotoImage(file = 'image/china.gif') # icon in calculator window, because why not?
		#root.tk.call('wm', 'iconphoto', root._w, img)
		self.display = Label(root, text = self.displayVal) # display is a label because they don't need to type
		self.display.grid(row = 1, columnspan = 4) # gridded seperately and stored in variable because access is needed later
		Button(root, text = 'Enter', command = self.enter).grid(row = 2, column = 1) # other buttons, don't need access later so no variable name
		Button(root, text = 'Clear', command = self.clearall).grid(row = 2, column = 2)
		Button(root, text = 'Store', command = self.inMem).grid(row = 2, column = 3)
		Button(root, text = 'Mem', command = self.outMem).grid(row = 2, column = 4)
		Button(root, text = '   *   ', command = self.multiply).grid(row = 3, column = 1)
		Button(root, text = '   /   ', command = self.divide).grid(row = 4, column = 1)
		Button(root, text = '  +   ', command = self.add).grid(row = 5, column = 1)
		Button(root, text = '   -   ', command = self.subtract).grid(row = 6, column = 1)
		Button(root, text = '   7   ', command = self.seven).grid(row = 3, column = 2)
		Button(root, text = '   8   ', command = self.eight).grid(row = 3, column = 3)
		Button(root, text = '   9   ', command = self.nine).grid(row = 3, column = 4)
		Button(root, text = '   4   ', command = self.four).grid(row = 4, column = 2)
		Button(root, text = '   5   ', command = self.five).grid(row = 4, column = 3)
		Button(root, text = '   6   ', command = self.six).grid(row = 4, column = 4)
		Button(root, text = '   1   ', command = self.one).grid(row = 5, column = 2)
		Button(root, text = '   2   ', command = self.two).grid(row = 5, column = 3)
		Button(root, text = '   3   ', command = self.three).grid(row = 5, column = 4)
		Button(root, text = '  del ', command = self.delete).grid(row = 6, column = 4)
		Button(root, text = '    .   ', command = self.dot).grid(row = 6, column = 3)
		Button(root, text = '   0   ', command = self.zero).grid(row = 6, column = 2)
		root.mainloop() #make the window appear
		return

	##### number buttons each have there own functions, essentially a way to pass their number to change display #####
	def one(self):
		self.addToDisplay('1')
		return

	def two(self):
		self.addToDisplay('2')
		return
		
	def three(self):
		self.addToDisplay('3')
		return
		
	def four(self):
		self.addToDisplay('4')
		return
		
	def five(self):
		self.addToDisplay('5')
		return
		
	def six(self):
		self.addToDisplay('6')
		return
		
	def seven(self):
		self.addToDisplay('7')
		return

	def eight(self):
		self.addToDisplay('8')
		return
		
	def nine(self):
		self.addToDisplay('9')
		return
		
	def zero(self):
		self.addToDisplay('0')
		return
		
	def dot(self): # can add decimals and floats
		if self.new:
			self.changeDisplay('0.') # can just type a . instead of 0.
		elif '.' in self.displayVal: # makes sure they aren't trying to put multiple .'s in a number
			doNothing = True
		else:
			self.changeDisplay('.')
		return
		
	def delete(self): # get rid of number in current display
		self.new = True
		self.changeDisplay('0')
		self.new = True
		return

	def enter(self): # add number in display to stack
		if self.new == False: # if the number isn't a new one then don't add it to the stack
			floatBool = True # assume it's a float
			localDisplayVal = self.displayVal # get the displayVal and store it in a local variable
			if localDisplayVal[len(localDisplayVal) - 1] == '.': # check to see if it ends in a .
				localDisplayVal = localDisplayVal + '0' # if it does, append a zero so it's treated as a float
			elif '.' not in localDisplayVal: # if it doesn't have a . we'll treat it as an int
				floatBool = False
			if floatBool: # if it is a float, add to stack as float
				valToPush = float(localDisplayVal)
			else:
				valToPush = int(localDisplayVal) # otherwise we add to stack as an int
			self.push(valToPush) # add to stack
			self.new = True # next number entered will replace current display number
		return

	def addToDisplay(self, num): # method to change the display
		self.displayVal = self.displayVal + num # otherwise append the number to what is already there
		self.display['text'] = self.displayVal # update what is in the display
		if num == '*' or num == '/' or num == '+' or num == '-':
			self.number += num
		return

	def changeDisplay(self, num):
		self.displayVal = num
		self.display['text'] = self.displayVal
		return

	def clearall(self): # clears entire stack/memory
		for node in range(self.size - 1): # pops all nodes off stack
			self.pop()
		self.changeDisplay('0')
		self.new = True # next thing typed will replace
		return

	def inMem(self): # puts value in display in memory
		self.memory = self.displayVal
		return

	def outMem(self): # puts value in memory in display
		self.changeDisplay(self.memory)
		return

	def multiply(self): # multipy operator
		self.addToDisplay('*')
		if '.' in self.number:
			self.enqueue(float(self.number))
		else:
			self.enqueue(int(self.number))
		self.enqueue('*')
		return

	def divide(self): # division operator
		self.addToDisplay('/')
		if '.' in self.number:
			self.enqueue(float(self.number))
		else:
			self.enqueue(int(self.number))
		return

	def add(self): # addition operator
		self.addToDisplay('+')
		if '.' in self.number:
			self.enqueue(float(self.number))
		else:
			self.enqueue(int(self.number))
		return

	def subtract(self): # subtraction operator
		self.addToDisplay('-')
		if '.' in self.number:
			self.enqueue(float(self.number))
		else:
			self.enqueue(int(self.number))
		return

pole = calc() # start the calculator
# wanted to find a way to use calc.exe but couldn't :(