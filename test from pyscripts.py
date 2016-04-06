# while True:
# 	built = ""
# 	inny = ""

# 	while (inny != "quit"):
# 		built += inny
# 		inny = input()

# 	print(built)

N = input()
R1 = []
for c in N[0:3]:
	R1.append(int(c))
S1 = sum(R1)
print(S1)