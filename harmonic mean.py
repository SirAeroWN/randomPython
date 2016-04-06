import matplotlib.pyplot as plt

def harm(x, y):
	return ((2*x*y) / (x + y))

def mean(x, y):
	return ((x + y) / 2)

def fakeRMS(x, y):
	return (((x**2 + y**2)**0.5) / 2)

def getData(foo, r, d):
	l = []
	for i in range(1, r):
		l.append(foo(i, i + d))
	return l


#for i in range(1, 1000):
#	print(3/i, " | ", mean(i, i + 3) - fakeRMS(i, i + 3))

plt.plot(range(1,1000), getData(mean, 1000, 3), 'r--', range(1,1000), getData(fakeRMS, 1000, 3), 'bs')
plt.show()