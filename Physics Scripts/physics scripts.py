import math
from tkinput import tkinput


def distance(v, angle):
    Yv = math.sin(math.radians(angle)) * v
    Xv = math.cos(math.radians(angle)) * v
    # print(Yv, Xv)
    t = (Yv / 9.8)
    # print(2 * t)
    return Xv * t * 2


def hieght(v, angle):
    Yv = math.sin(math.radians(angle)) * v
    t = (Yv / 9.8)
    return Yv * t


def slope(x1, x2, y1, y2):
    dx = x2 - x1
    dy = y2 - y1
    return dy / dx


v1 = 2.56
v2 = 3.56
r1 = distance(v1, 45)
r2 = distance(v2, 45)
r3 = distance(v1, 45) * 0.97
r4 = distance(v2, 45) * 0.95
# print("slope", slope(v1**2, v2**2, r3, r4)**-1)
# print(2.56, distance(v1, 45) * 0.97)
# print(3.56, distance(v2, 45) * 0.95)

v = 9.495262
# print(15, distance(v, 15), hieght(v, 15))
# print(30, distance(v, 30), hieght(v, 30))
# print(45, distance(v, 45), hieght(v, 45))
# print(15, distance(v, 60), hieght(v, 60))
# print(30, distance(v, 75), hieght(v, 75))

# a = 71.7
# while a < 72.0:
#     print(a, distance(21, a))
#     a += 0.01

print(float(tkinput("Enter initial velocity:")), float(tkinput("Enter starting angle w.r.t. horizontal:")))


#print(float(tkinput("test")))
