mass = 12500 #25038.3
area = 6.55 * 3.6
rho = 1.247
C = 1
v = 0.0 #v[0] is the previous velocity, v[1] is the current velocity |||| not sure i actually need this but meh
a = 9.8
t = 0.0
step = 0.00001
Fgrav = mass * a

while t <= 24:
	Fdrag = (((0.5) * rho * C * area * (v**2)))
	v = v + (((Fgrav - Fdrag) / mass) * step)
	t += step

print(v)
print(v * (3600/1000))