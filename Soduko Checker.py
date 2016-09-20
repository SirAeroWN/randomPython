def checkDirection(square, start, x, y):
	s = 0
	for i in range(3):
		s += square[start[0]+(i*x)][start[1]+(i*y)]
	if s == 15:
		return True
	else:
		return False

def checkTheStuffs(square):
	for row in range(3):
		if not checkDirection(square, [0,row], 1, 0):
			print("Failed on row", row)
			return

	for col in range(3):
		if not checkDirection(square, [col,0], 0, 1):
			print("Failed on column", col)
			return

	if not checkDirection(square, [0,0], 1, 1):
		print("Failed on diagonal 1")
		return

	if not checkDirection(square, [2,0], -1, 1):
		print("Failed on diagonal 2")
		return

	print("works")

n = input()
n = n.split(" ")
n = [int(num) for num in n]
square = [n[0:3], n[3:6], n[6:10]]
checkTheStuffs(square)
