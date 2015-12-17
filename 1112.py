# # 6.1 classwork
# n=int(input('Enter number of elements: '))
# def sum(l):
#     fi += 1/(l**2 + 1)
#     return fi
# i=0
# while i<=n:
#     p=
#
# def d(l):
#     n = int(input())
#     i = 0
#     while i < n:
#         i+=1
#         s = 1/(i**2 +1)
#     return s
# n = int(input())
# p = 1
# while i < n:
#     p *= d(i)


# 6.1 (2)
def p(n):
    l = 0
    p = 1
    while l <= n:
        f = 0
        i = 1
        while i <= l+1:
            f += 1/(l**2 + i)
            i += 1
        l += 1
        p *= f
    return p
n = int(input('n = '))
print(p(n))

# 6.2
def blyz(n):
    i = n+1
    while i < n*2:
        print(i-1, i+1)
        i += 1
m = int(input("n > 2, n = "))
if m <= 2:
    print('invalid move')
else:
    blyz(m)

# 6.3
# a
def kvdr(t):
    p = []
    for i in range(1, t+1):
        for j in range(1, t//2):
            if j**2 == i:
                p.append(i)
    return p
# b
def pyt(t):
    p = []
    for i in range(1, t+1):
        for j in range(1, t//5):
            if 5**j == i:
                p.append(i)
    return p
# c
def prst(a):
    p = []
    for i in range(1, a+1):
        d = 'yes'
        for j in range(2, i):
            if i%j == 0:
                d = 'no'
                break
        if d == 'yes':
            p.append(i)
    return p
n = int(input('n = '))
print(kvdr(n), pyt(n), prst(n))

# 6.6
def root(x, k, e):
    y0 = 1
    y1 = y0 + (x/y0**(k-1) - y0)/k
    while abs(y1 - y0) >= e:
        y0 = y1
        y1 = y0 + (x/y0**(k-1) - y0)/k
    return y1
a = float(input('a = '))
e = float(input('enter epsilon: '))
c = root(a, 3, e) - root((a**2 +1), 6, e)
d = 1 + root((3+a), 7, e)
print(c/d)

# 6.8
x = float(input('x = '))
a = abs(x)
b = a - int(a)
if 0 <= b < 0.25:
    y = b
if 0.25 <= b < 0.75:
    y = -(b - 0.5)
if 0.75 <= b < 1:
    y = b - 1

if x < 0:
    y = -y

print(y)
print('vidpovid\': niyakyh ne treba pidprogram')

# 6.23
# a)
def a(x):
    if x < 10**(-6):
        return 0
    # print(x)
    return a(x/2) + x**(1/2)
print(a(float(input('x = '))))
# b)
def b(x):
    if x > 10**3 or x < 10**(-6):
        return 0
    return b(x + 1) + 1/x
print(b(float(input('x = '))))
# as for my IDE it doesn't work if x > 0.0000001 or <= 3, too much recursion it writes
# c)
from math import log
def c(x):
    if x <= 10**(-6):
        return 0
    return c(log(x)) + log(x)
print(c(float(input('x = '))))
# d)
def d(x):
    if 1/2 <= x <= 2**10:
        return d(x*2) + d(x/2)
    else:
        return x
    # if x < 1/2 or x > 2**10:
    #     return x
    # return d(x*2) + d(x/2)
print(d(float(input('x = '))))
# doesn't work too, but looks like all right

# 6.25
def nsd(n, m):
    if n <= 0 or m <= 0:
        return 'invalid move'
    if n == m:
        return n
    if m > n:
        m, n = n, m
    r = n%m
    if r == 0:
        return m
    return nsd(m, r)
import random
for i in range(1, 12, 2):
    l = [a for a in range(1, 100) if a%i == 0]
    k = [a for a in range(1, 100) if a%(i+1) == 0]
    a = random.choice(l)
    b = random.choice(k)
    print(a, b, ':', nsd(a, b))

# 6.27
import random
def pwr(a, z):
    if z == 0:
        return 1
    if z < 0:
        return 1/pwr(a, abs(z))
    if z > 0:
        return a*pwr(a, z-1)
for i in range(6):
    a = random.choice(range(2, 20))
    if a > 10:
        b = 2
    else:
        b = random.choice(range(2, 4))
    print(a, '**', b, '=', pwr(a, b))

# 7.40
# a)
def aa(*args):
    if all(args[i - 1] > args[i] for i in range(1, len(args))):
        return 0
    else:
        sum = 0
        for i in range(1, len(args)):
            k = args[i] - args[i - 1]
            sum += abs(k)
        return sum

import random
n = [i for i in range(10)]
k = [n.pop(random.choice(range(10))), n.pop(random.choice(range(9))), n.pop(random.choice(range(8))), n.pop(random.choice(range(7))), n.pop(random.choice(range(6)))]
l = k.copy()
l.sort()
l.reverse()
print(k, aa(*k), '\n', l, aa(*l))
# b)
def bb(*args):
    if all(args[i - 1] <= args[i] for i in range(1, len(args))):
        return 1
    else:
        sum = 0
        for i in range(len(args)-1):
            k = 2**(args[i] + args[i+1])
            sum += k
        return sum
import random
k = [random.choice(range(10)) for i in range(random.choice(range(4,7)))]
l = k.copy()
l.sort()
print(k, bb(*k), '\n', l, bb(*l))
# c)
def cc(*args):
    if all(args[i] <= 2**(i+1) for i in range(len(args))):
        return 0
    p = 1
    for i in range(len(args)):
        p *= args[i]
    return p
import random
k = [random.choice(range(10)) for i in range(random.choice(range(1,5)))]
print(k, cc(*k))
# d)
def dd(*args):
    if max(args) > sum(args) - max(args):
        return 1
    res = 0
    for i in args:
        if i > 0:
            res += i
    return res
import random
k = [random.choice(range(20)) for i in range(random.choice(range(1,5)))]
print(k, dd(*k))

# 7.166
def find(f, a, b, e = 0.01):
    if a >= b or f(a) > 0 and f(b) > 0 or f(a) < 0 and f(b) < 0:
        return 'invalid move'
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    c = (a + b)/2
    if f(c) == 0:
        return c
    if f(a) > 0 and f(c) < 0 or f(a) < 0 and f(c) > 0:
        if abs(a - c) > e:
            return find(f, a, c, e)
        else:
            return (a, c)
    if f(b) > 0 and f(c) < 0 or f(b) < 0 and f(c) > 0:
        if abs(b - c) > e:
            return find(f, c, b, e)
        else:
            return (c, b)
def func(x):
    return x**3 - 7*x - 1

print(find(func, -3, -2), find(func, -1, 1), find(func, 2, 3))
import random
e = random.choice([0.001, 0.0001, 0.00001])
print('e =', e, find(func, -1, 1, e))

# homework
# 6.14
def frstsym(s, a):
    if len(a) != 1 or s != str(s):
        return 'invalid move'
    for i in range(len(s)):
        if s[i] == a:
            return i
def lstsym(s, a):
    if len(a) != 1 or s != str(s):
        return 'invalid move'
    c = s[::-1]
    for i in range(len(c)):
        if c[i] == a:
            return (len(s)-1) - i
l = 'abcdefghijklmnopqrstuvwxyz'
print(l)
import random
x = random.choice(l)
y = random.choice(l)
z = random.choice(l)
print('letter {}: first {}, last {}, letter {}: first {}, last {}, letter {}: first {}, last {}'.format(x, frstsym(l,x), lstsym(l,x), y, frstsym(l,y), lstsym(l,y), z, frstsym(l,z), lstsym(l,z)))

# 6.15
def z10(s, a):
    d = ''
    for i in range(a, len(s)):
        if s[i] == '1':
            s = s[:i] + '0' + s[i+1:]
            continue
        if s[i] == '0':
            s = s[:i] + '1' + s[i+1:]
    return s
d = '1010101111000111001010101010'
import random
b = random.choice(range(5, len(d)-5))
print(d, b, z10(d, b), sep = '\n')

# 6.21
def red(s):
    for i in range(len(s)-1):
        if s[i+1] == s[i]:
            s = s[:i] + s[i+1:]
        if i >= len(s)-2:
            break
    if len(s) <= 2:
        return s
    if all(s[i] != s[i+1] for i in range(len(s)-1)):
        return s
    else:
        return red(s)
h = input('enter string: ')
print(red(h))

# 6.22
def abcd(s):
    l = []
    w = ''
    for i in s:
        if i.isalpha(): # if "word" really means "word"
            w += i
        else:
            if w != '':
                l.append(w)
                w = ''
    if s[len(s)-1].isalpha():
        l.append(w)
    max = ''
    min = s
    p = []
    for i in l:
        if len(i) > len(max):
            max = i
        if len(i) < len(min):
            min = i
        if i == i[::-1]:
            p.append(i)
    return len(l), max, min, p
def e(s):
    l = []
    w = ''
    for i in s:
        if i.isnumeric():
            w += i
        else:
            if w != '':
                l.append(w)
                w = ''
    if s[len(s)-1].isnumeric():
        l.append(w)
    return l
def g(s):
    l = []
    w = ''
    for i in s:
        if i.isalnum() or i == '_':
            w += i
        else:
            if w != '':
                l.append(w)
                w = ''
    if s[len(s)-1].isalnum(): # i don't know whether they can end on "_"
        l.append(w)
    h = []
    for i in l:
        if i.isidentifier():
            h.append(i)
    return h
d = input('entr string: ')
print('a) the number of words - {} \nb) the longest word - \"{}\" \nc) the shortest word - \"{}\" \nd) palindromes: {} \ne) natural numbers: {} \ng) identifiers: {} # i don\'t know why it works so strange, but it\'s not my blame'.format(abcd(d)[0], abcd(d)[1], abcd(d)[2], abcd(d)[3], e(d), g(d)))

