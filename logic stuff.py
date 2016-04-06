def cross(A, B):
    prod = []
    for a in A:
        for b in B:
            prod.append([a, b])
    return prod

def printCross(C):
    for c in C:
        print(", (", c[0], ", ", c[1], ")", sep="", end="")

def rule1(A, B):
    prod = []
    for a in A:
        for b in B:
            if b % a == 0:
                prod.append([a, b])
    return prod

def rule2(A, B):
    prod = []
    for a in A:
        for b in B:
            if b == (a + 4):
                prod.append([a, b])
    return prod

def intersect(A, B):
    prod = []
    for a in A:
        if a in B:
            prod.append(a)
    return prod

def union(A, B):
    prod = []
    for a in A:
        prod.append(a)
    for b in B:
        if not (b in prod):
            prod.append(b)
    return prod

def circle(A, B):
    prod = []
    for a in A:
        for b in B:
            if a[1] == b[0]:
                prod.append([a[0], b[1]])
    return prod

def invertRelation(A):
    prod = []
    for a in A:
        prod.append([a[1], a[0]])
    return prod

def printCAll(l):
    for s in l:
        printCross(s)

# A = [2, 4]
# B = [6, 8, 10]
# C = cross(A, B)
# R = rule1(A, B)
# S = rule2(A, B)
# RUS = union(R, S)
# RNS = intersect(R, S)
# print("\nR", end=": ")
# printCross(R)
# print("\nS", end=": ")
# printCross(S)
# print("\nRUS", end=": ")
# printCross(RUS)
# print("\nRNS", end=": ")
# printCross(RNS)

# R = [[1,4],[1,6],[2,6],[3,5]]
# S = [[4,5],[4,6],[6,4],[5,5]]
# printCross(circle(S, invertRelation(S)))

T = [[1,2], [2,3], [1,3], [3,2], [2,1], [3,1]]
printCross(invertRelation(T))