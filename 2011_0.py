# #7.34 a)
# n = int(input('Enter number of elements: '))
# list=[]
# i = 0
# while i < n:
#     p = int(input('enter int: '))
#     list += [p]
#     i += 1
# l1 = [a for a in list if a%2 == 0]
# print(sum(l1))
# #b)
# n = int(input('Enter number of elements: '))
# list=[]
# i = 0
# while i < n:
#     p = int(input('enter int: '))
#     list += [p]
#     i += 1
# l1 = [a for a in list if a%2 != 0]
# print(sum(l1))
# #c)
# n = int(input('Enter number of elements: '))
# list=[]
# i = 0
# while i < n:
#     p = int(input('enter int: '))
#     list += [p]
#     i += 1
# l1 = [a for a in list if a > 0]
# print(sum(l1))
# #d)
# n = int(input('Enter number of elements: '))
# list=[]
# i = 0
# while i < n:
#     p = int(input('enter int: '))
#     list += [p]
#     i += 1
# l1 = [a for a in list if a < 0]
# print(sum(l1))

# #7.36 a)
# n = int(input('Enter number of elements: '))
# list=[]
# i = 0
# while i < n:
#     p = int(input('enter int: '))
#     list += [p]
#     i += 1
# print(sum(list)/n)
# #b)
# from math import sqrt
# n = int(input('Enter number of elements: '))
# list=[]
# i = 0
# while i < n:
#     p = int(input('enter int: '))
#     list += [p]
#     i += 1
# l1 = [a**2 for a in list]
# print(sqrt(sum(l1)))
# #c)
# from math import sqrt
# n = int(input('Enter n for n-dimensional space: '))
# list1 =[]
# print('enter dot one')
# i = 0
# while i < n:
#     p = int(input('enter int: '))
#     list1 += [p]
#     i += 1
# list2 =[]
# list1m2 = []
# print('enter dot two')
# i = 0
# while i < n:
#     p = int(input('enter int: '))
#     list2 += [p]
#     list1m2 += [(p - list1[i])**2]
#     i += 1
# absl1m2 = sqrt(sum(list1m2))
# print(absl1m2)
# #d
# n = int(input('Enter n for n-dimensional space: '))
# list1 =[]
# print('enter vector one')
# i = 0
# while i < n:
#     p = int(input('enter int: '))
#     list1 += [p]
#     i += 1
# list2 =[]
# d = 0
# print('enter vector two')
# i = 0
# while i < n:
#     p = int(input('enter int: '))
#     list2 += [p]
#     d += p * list1[i]
#     i += 1
# print(d)

#7.40 a)
n = int(input('enter number of variables: '))
list = []
i = 0
while i < n:
    p = float(input('enter element: '))
    list += [p]
    i += 1
j = 0
for i in range(n-1):
    if list[i] > list[i+1]:
        j += 1
f = 0
if j == n-1:
    pass
else:
    for i in range(n-1):
        j = abs(list[i+1] - list[i])
        f += j
print(f)
#b)
n = int(input('enter number of variables: '))
list = []
i = 0
while i < n:
    p = float(input('enter element: '))
    list += [p]
    i += 1
j = 0
for i in range(n-1):
    if list[i] <= list[i+1]:
        j += 1
f = 0
if j == n-1:
    f = 1
else:
    for i in range(n-1):
        j = 2**(list[i+1] + list[i])
        f += j
print(f)
#h)
n = int(input('enter number of variables: '))
listx = []
i = 0
f = 1
while i < n:
    print('enter x', i, ': ', sep = '')
    p = float(input())
    listx += [p]
    i += 1
listy = []
i = 0
while i < n:
    print('enter y', i, ': ', sep = '')
    p = float(input())
    listy += [p]
    f *= (listx[i]**3 + p**3)
    i += 1
print(f)

#7.41
n = int(input('the number of rows/columns: '))
A = []
for i in range(n):
    A.append([])
    for j in range(n):
        print('element', i, j)
        x = float(input())
        A[i].append(x)
t = 0
for i in range(n):
    t += A[i][i]
print(t)

#7.43 a)
n = int(input('the number of rows: '))
m = int(input('the number of columns: '))
A = []
s = 0
for i in range(n):
    A.append([])
    for j in range(m):
        print('element', i, j)
        x = float(input())
        A[i].append(x)
        if j != i:
            s += A[i][j]
print(s)
#b)
k = 0
A = []
n = int(input('the number of rows: '))
m = int(input('the number of columns: '))
for i in range(n):
    A.append([])
    for j in range(m):
        print('element', i, j)
        x = float(input())
        A[i].append(x)
        if A[i][j] == 0:
            k += 1
print(k)

#7.44 a)
n = int(input('enter n for n-dimensional space: '))
v1 =[]
print('enter vector one')
i = 0
while i < n:
    p = float(input('enter float: '))
    v1 += [p]
    i += 1
v2 =[]
d = []
print('enter vector two')
i = 0
while i < n:
    p = float(input('enter float: '))
    v2 += [p]
    d += [p + v1[i]]
    i += 1
print(d)
#b)
n = int(input('enter n for n-dimensional space: '))
i = 0
v = []
print('enter vector')
while i < n:
    p = float(input('enter float: '))
    v += [p]
    i += 1
l = float(input('enter scalar: '))
l1 = [a*l for a in v]
print(l1)
