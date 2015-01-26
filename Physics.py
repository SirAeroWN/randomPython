#This is a file some classes to emulate physics
#The idea is that there is a list which contains particle objects, each which know where they are
##Eventually, some spots in the list will be empty and particles can move

class Particle:
	def __init__(self, x = 0, y = 0, z = 0, mass = 1, velocity = 0):
		self.x = x
		self.y = y
		self.z = z
		self.mass = mass
		self.velocity = velocity
		self.add()
		return

	def __str__(self):
		point = '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'
		return point

	def add(self):
		global world
		world.append(self)

	def findYRelative(self, deltaY):
		global world
		found = False
		for part in world:
			if part.y == self.y + deltaY and part.x == self.x and part.z == self.z:
				found = True
				return part
		if not found:
			return None

	def findXRelative(self, deltaX):
		global world
		found = False
		for part in world:
			if part.y == self.y and part.x == self.x + deltaX and part.z == self.z:
				found = True
				return part
		if not found:
			return None

	def findZRelative(self, deltaZ):
		global world
		found = False
		for part in world:
			if part.y == self.y and part.x == self.x and part.z == self.z + deltaZ:
				found = True
				return part
		if not found:
			return None

	def findXYZRelative(self, deltaX, deltaY, deltaZ):
		global world
		found = False
		for part in world:
			if part.y == self.y + deltaY and part.x == self.x + deltaX and part.z == self.z + deltaZ:
				found = True
				return part
		if not found:
			return None

def worldPrint():
	global world
	for i in world:
		print(i)

world = []

a = Particle()
b = Particle(1,1,1,1,0)
worldPrint()
print(b.findXYZRelative(-1,-1,-1))