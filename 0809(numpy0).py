import numpy as np
import random

print('# 20.12')
def up_tr(a):
    s = a.shape
    for i in range(s[0]):
        for j in range(s[1]):
            if i > j and a[i, j] != 0:
                return False
            if i <= j and a[i, j] == 0:
                return False
    return True

def down_tr(a):
    s = a.shape
    for i in range(s[0]):
        for j in range(s[1]):
            if i < j and a[i, j] != 0:
                return False
            if i >= j and a[i, j] == 0:
                return False
    return True

a = np.array([[1, 0, 0], [1, 1, 0], [1, 1, 1]])
print(a)
print('upper triangular matrix ', up_tr(a))
print('lower triangular matrix ', down_tr(a))
b = a.transpose()
print(b)
print('upper triangular matrix ', up_tr(a))
print('lower triangular matrix ', down_tr(a))

print('# 20.13')
def dist(a, b):
    return np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2).round(1)
np.vectorize(dist)

n = random.choice(range(3, 6))
a = np.random.rand(n, 2)*10//1

l1, l2 = [], []
for i in range(n):
    for j in range(i+1, n):
        l1.append(i)
        l2.append(j)
l1, l2 = np.array(l1), np.array(l2)

c = np.zeros((l1.size)*4)
c.shape = (l1.size, 2, 2)
c[:,0] = a[l1]
c[:,1] = a[l2] # i don't know for wtf i need 3dim array, but it was in the task

d = dist(a[l1].transpose(), a[l2].transpose())
i = [i for i in range(len(l1)) if d[i] == d.max()]

print(a, '- random dots\n')
# print(l1)
# print(l2) # index arrays
print(c, '- couple dots\n')
# print(d) # all dist
# print(i)
print(c[i], 'max distance =', d[i], '\n')


print('# 20.14')
def per(a, b, c):
    return (np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2) + np.sqrt((a[0]-c[0])**2 + (a[1]-c[1])**2) + np.sqrt((c[0]-b[0])**2 + (c[1]-b[1])**2)).round(1)
np.vectorize(per)

n = random.choice(range(4, 6))
a = np.random.rand(n, 2)*10//1

l = []
for i in range(n):
    for j in range(i+1, n):
        for h in range(j+1, n):
            l.append([i, j, h])
l = np.array(l)
l0, l1, l2 = np.array(l[:,0]), np.array(l[:,1]), np.array(l[:,2])
sz = l0.size

c = np.zeros(sz*6)
c.shape = (sz, 3, 2)
c[:,0] = a[l0]
c[:,1] = a[l1]
c[:,2] = a[l2]

p = per(a[l0].transpose(), a[l1].transpose(), a[l2].transpose())

i = [i for i in range(sz) if p[i] == p.max()]

print(a, '- dots\n')
print(c, '- triangles\n')
# print(p) # all perimeters
print(c[i], 'max perimeter =', p[i], '\n')

print('# 20.15')
def dist0(a, b):
    return np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2).round(0)
np.vectorize(dist0)

def equil(d):
    e = np.zeros(len(d))
    for i in range(len(d)):
        if d[i,0] == d[i,1] and d[i,1] == d[i,2] and d[i,0] == d[i,2]:
            e[i] = d[i,0]
    return e


n = random.choice(range(4, 36))
a = np.random.rand(n, 2)*10//1


l = []
for i in range(n):
    for j in range(i+1, n):
        for h in range(j+1, n):
            l.append([i, j, h])
l = np.array(l)
l0, l1, l2 = np.array(l[:,0]), np.array(l[:,1]), np.array(l[:,2])
sz = l0.size

c = np.zeros(sz*6)
c.shape = (sz, 3, 2)
c[:,0] = a[l0]
c[:,1] = a[l1]
c[:,2] = a[l2]

d = np.zeros(sz*3)
d.shape = (3, sz)
d[0] = dist0(a[l1].transpose(), a[l0].transpose())
d[1] = dist0(a[l1].transpose(), a[l2].transpose())
d[2] = dist0(a[l0].transpose(), a[l2].transpose())
d = d.transpose()

e = equil(d)
i = [i for i in range(sz) if e[i] != 0]

print(a, '- dots\n')
print(c, '- triangles\n')
print(c[i], '- equilateral triangles')