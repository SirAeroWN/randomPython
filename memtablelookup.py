# simple interface for getting a specific entry

memoryStr = ["d5 f8	c5	ae	bf	10	6b	66	26	e3	51	e6	c8	70	c6	af",
"3f	26	ef	76	4d	6c	51	e6	d9	da	6c	48	0f	48	7b	e4",
"40	40	92	00	51	fd	67	77	e1	b8	5d	a9	29	23	59	69",
"4a	48	e0	98	b5	31	7e	8e	0b	ea	d6	1a	33	52	ff	73",
"92	91	73	e3	8f	db	5b	71	93	b8	1b	bc	dc	75	25	26",
"be	06	be	73	37	3d	01	43	28	d8	5e	5b	2a	5d	cf	bd",
"ef	42	a1	7f	1e	fc	f1	b1	b4	0d	6e	91	82	94	b8	40",
"9a	77	b4	d2	b4	b6	15	dc	8f	73	38	b9	d0	07	77	c0",
"4a	18	3f	68	14	30	19	c9	3d	88	5b	c0	1d	13	01	b7",
"8a	b5	8a	3f	6b	9f	1c	fb	13	54	b5	e4	5b	2c	a4	a5",
"45	e4	0d	59	14	27	23	52	b0	7e	13	cd	92	14	85	1d",
"c9	0f	5c	35	af	79	30	c2	cd	e5	a6	29	12	4a	cf	57",
"2f	dd	b1	43	04	d4	96	b5	53	a9	82	e5	bd	07	02	87",
"17	5f	bd	c6	d8	ed	88	a6	d3	2e	cf	e5	79	9f	3d	a8",
"7c	ee	ec	81	c2	83	36	15	2c	b8	fb	ea	c0	fd	71	d7",
"5d	2e	9d	35	1c	26	db	f0	54	ab	d6	ce	4b	13	77	c7"]

memory = []
for page in memoryStr:
	memory.append(page.split())

# for i in range(16):
# 	for j in range(16):	
# 		print(memory[i][j], end="")
# 		if (j == 15):
# 			print(memory[i + 1][0])
# 		else:
# 			print(memory[i][j + 1])

va = input("address: ").strip()
while va != "q":
	# print(memory[int(req[0], 16)][int(req[1], 16)], end="")
	# print(memory[int(req[0], 16)][int(req[1], 16) + 1])

	vpn = va[0];
	offset = int(va[1], 16);
	pte = memory[0][int(vpn, 16)]
	if(int(pte[0], 16) >= 8):
		print("fault")
	else:
		print(memory[int(pte[1], 16)][offset + 1], memory[int(pte[1], 16)][offset], sep="")

	va = input("address: ").strip()

req = input("address: ").strip()
while req != "q":
	print(memory[int(req[0], 16)][int(req[1], 16) + 1], end="")
	print(memory[int(req[0], 16)][int(req[1], 16)])

	req = input("address: ").strip()