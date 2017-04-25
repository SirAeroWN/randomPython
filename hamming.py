# 1 1 1 0 0 0 1 0 1 0 0 0
# 1 0 0 1 1 0 1 1 0 1 0 0
# 0 1 0 1 0 1 1 1 0 0 1 0
# 0 0 1 0 1 1 0 1 0 0 0 1
# 1 0 0 1 1 0 0 0

def s(R, pm, p):
	ms = ""
	for c in pm:
		ms += str(c)
	for c in p:
		ms += str(c)
	m = []
	for c in ms:
		m.append(int(c))
	#print("message with parity:", m)
	t = []
	for i in range(len(R)):
		t.append(int(R[i]) & int(m[i]))
	#print("result of &:", t)
	ans = int(t[0])
	for j in range(1, len(R)):
		ans = int(ans) ^ int(t[j])
	return ans

def inc(p):
	s = ""
	for c in p:
		s += str(c)
	b = int(s, 2)
	b += 1
	s = str(bin(b))[2: ]
	while (len(s) < 4):
		s = "0" + s
	g = []
	for c in s:
		g.append(int(c))
	return g

row1 = [int(c) for c in "1 1 1 0 0 0 1 0 1 0 0 0".strip().split()]
row2 = [int(c) for c in "1 0 0 1 1 0 1 1 0 1 0 0".strip().split()]
row3 = [int(c) for c in "0 1 0 1 0 1 1 1 0 0 1 0".strip().split()]
row4 = [int(c) for c in "0 0 1 0 1 1 0 1 0 0 0 1".strip().split()]
M = [int(c) for c in "1 0 0 1 1 0 0 0".strip().split()]
parity = [0,0,0,0]
#print("working")

s1 = s(row1, M, parity)
s2 = s(row2, M, parity)
s3 = s(row3, M, parity)
s4 = s(row4, M, parity)

while(True):
	parity = inc(parity)
	if (len(parity) > 4):
		break
	s1 = s(row1, M, parity)
	s2 = s(row2, M, parity)
	s3 = s(row3, M, parity)
	s4 = s(row4, M, parity)
	print(parity, s1, s2, s3, s4)
	if (s1 == 0 and s2 == 0 and s3 == 0 and s4 == 0):
		print("got it:", parity)