#classwork
A = []
n = int(input('the number of rows/columns: '))
for i in range(n):
    A.append([])
    for j in range(n):
        print('element', i, j)
        x = float(input())
        A[i].append(x)
print(A)
for i in range(n):
    for j in range(n):
        if A[i][j]==A[j][i]:
            res = 'Symmetric'
        else:
            res = 'Not symmetric'
            break
print(res)

import random
c = random.choice(['kresta', 'bubna', 'chirva', 'pika'])
print("kozyr = ", c)
a=random.choice([2,3,4,5,6,7,8,9,10,11,12,13,14])
b=random.choice(['kresta', 'bubna', 'chirva', 'pika'])
k1 = (a,b)
print('k1 = ', k1)
k2 = k1
while k2 == k1:
    a=random.choice([2,3,4,5,6,7,8,9,10,11,12,13,14])
    #b=random.choice(['kresta', 'bubna', 'chirva', 'pika'])
    k2 = (a, b)
print('k2 = ', k2)
if k1[1] == c and k2[1] != c:
    print("k1 win!")
if k2[1] == c and k1[1] != c:
    print('k2 win!')
if k1[1] == k2[1]:
    if k1[0] > k2[0]:
        print('k1 win.')
    else:
        print('k2 win')

#homework
# 7.83
import random
from collections import namedtuple
stud = namedtuple('stud', ['surname', 'group', 'test1', 'test2', 'test3'])
A = ['Blyznyk', 'Kyslyak', 'Levandovsky', 'Lytovkina', 'Lomako', 'Lukashuk', 'Musienko', 'Rybakova', 'Savchuk', 'Hohlov', 'Shatrov', 'Yankovska']
g = []
for i in A:
    p = stud(i, 'stat', random.choice([0, 1, 2, 3, 4, 5]), random.choice([0, 1, 2, 3, 4, 5]), random.choice([3, 4, 5]))
    # test3 was very easy test
    g.append(p)
print(g)
borg = []
vidm = []
t1 = t2 = t3 = 0
for i in g:
    if i.test1 == 0 or i.test2 == 0 or i.test3 == 0:
        borg.append(i.surname)
    if i.test1 >= 4 and i.test2 >= 4 and i.test3 >= 4:
        vidm.append(i.surname)
    t1 += i.test1
    t2 += i.test2
    t3 += i.test3
max = []
if t1 >= t2 and t1 >= t3:
    max.append('test1')
if t2 >= t1 and t2 >= t3:
    max.append('test2')
if t3 >= t1 and t3 >= t2:
    max.append('test3')
print('borzhnyky: ', borg, '\n', 'vidminnyky: ', vidm, '\n', 'naykrashe sdano: ', max)

#t7.1
import random
A = []
n = int(input('the number of rows/columns: '))
for i in range(n):
    A.append([])
    for j in range(n):
        x = random.choice(range(30))
        A[i].append(x)
print(A)
print(min(list(map(max, *A))))
#min z max znachen' po ryadkah, jak v umovi
B = list(map(list, zip(*A)))
print(min(list(map(max, *B))))
#min z max po stovpcyah, jak v pidkazci

#t7.2
A = []
n = int(input('the number of rows/columns: '))
for i in range(n):
    A.append([])
    for j in range(n):
        print('element', i, j)
        x = float(input())
        A[i].append(x)
if A == list(map(list, zip(*A))):
    print('symmetry')
else:
    print('not symmetry')

# t7.4
import random
A = []
n = int(input('the number of rows/columns: '))
for i in range(n):
    A.append([])
    for j in range(n):
        x = random.choice(range(10))
        A[i].append(x)
print(*A, sep = '\n')
l = [A[i][i] for i in range(n)]
print(sum(l))