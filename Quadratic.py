a = float(input('a= ').strip())
b = float(input('b= ').strip())
c = float(input('c= ').strip())

x1 = ((-1)*b + (b**2 - 4*a*c)**0.5)/(2*a)
x2 = ((-1)*b - (b**2 - 4*a*c)**0.5)/(2*a)

print('x = {}, {}'.format(x1, x2))