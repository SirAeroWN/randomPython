x = int(input("Enter x: "))
y = int(input("Enter y: "))

while y > 125:
	print(x, " = ", "(", x // y, ")", y, " + ", x % y, sep="")
	tx = y
	y = x % y
	x = tx