import random

class Numbers:
    def __init__(self, n):
        self.n = n
        self.start = 0

    def __iter__(self):
        return Test(self.n)


class Test:
    def __init__(self, n):
        self.n = n
        self.start = 0

    def __next__(self):
        if self.start >= self.n:
            raise StopIteration()
        a = self.start
        self.start += 1
        return a

# a = Numbers(10)
# for i in a:
#     print(i)

class Numbers2:
    def __init__(self, n):
        self.n = n
        # self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 0:
            raise StopIteration()
        a = self.n
        self.n -= 1
        return a

# a = Numbers(10)
# for i in a:
#     print(i)

class fib:
    def __init__(self, n):
        self.n = n
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.b >= self.n:
            raise StopIteration()
        self.a, self.b = self.b, self.a + self.b

        return self.a



# a = fib(100)
# for i in a:
#     print(i)


def fib():
    a, b = 1, 1
    while True:
        yield b
        a, b = b, a + b

# i = 1
# n = 1000
# for a in fib():
#     print(a)
#     i += 1
#     if i == n:
#         break

class List:
    def __init__(self):
        self.start = 0
        self.l = [1, 2, 3, None, 7, 8, 9, None, None, 21, 22, 23, None]

    def __iter__(self):
        return self

    def __next__(self):
        a = self.start
        while l[a] is None:
            self.l.next()
        if a == len(self.l):
            raise StopIteration()

        self.start += 1
        return l[a]

# s = List()
# for i in s:
#     print(i)


# homework

class String:
    def __init__(self, s):
        self.start = 0
        self.s = s.split()

    def __iter__(self):
        return self

    def __next__(self):
        a = self.start
        if a == len(self.s):
            raise StopIteration()
        self.start += 1
        return self.s[a]

class String2(String):
    def __next__(self):
        if self.s == []:
            raise StopIteration()
        a = self.s[0]
        for i in self.s:
            if len(i) < len(a):
                a = i
        y = a
        self.s.remove(a)
        return y

class String3(String):
    def __next__(self):
        if self.s == []:
            raise StopIteration()
        a = self.s[0]
        for i in self.s:
            if len(i) > len(a):
                a = i
        y = a
        self.s.remove(a)
        return y

print('# 16.11 a)')
s = String('The quick brown fox jumps over the lazy dog')
for i in s:
    print(i)
print()
print('c)')
s = String2('The quick brown fox jumps over the lazy dog')
for i in s:
    print(i)
print()
print('d)')
s = String3('The quick brown fox jumps over the lazy dog')
for i in s:
    print(i)
print()

print('# 16.14')
def mxn(m, n):
    assert m > 0 and n > 0
    for i in range(n):
        for j in range(m):
            yield random.choice(range(-50, 50))
l = []
c = (int(input('m = ')), int(input('n = ')))
try:
    for a in mxn(c[0], c[1]):
        print(a)
        l.append(a)
    print('a)', sum(l))
    print('b)', min(l))
    print('c)', max(l))
except AssertionError:
    print('try again')
print()

print('# 16.17 \ny = arcsin x')
def arcsingen(x):
    a = 1
    i = 1
    while True:
        z = (x**i/i) * a
        i += 2
        a *= (i-2)/(i-1)
        yield z

def arcsin(x, e = 0.001):
    assert abs(x) < 1
    ag = arcsingen(x)
    s = 0
    while True:
        z = next(ag)
        if z < e:
            return s
        s += z

x = float(input('x = '))
try:
    print(arcsin(x))
except AssertionError:
    print('try again and |x| < 1')