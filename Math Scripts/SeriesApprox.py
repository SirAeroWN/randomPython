def f(n,x):
	return (((-1)**n)*((x**(n+1)) / (n+1)))

def approx(n,x,error):
	val = f(n,x)
	if abs(val) < error:
		print(n)
		return 0
	else:
		return val + approx(n+1,x,error)

print(approx(0,0.5,0.0001))