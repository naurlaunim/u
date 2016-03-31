class QueueEl():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.bg = self.en = None

    def is_empty(self):
        return self.bg is self.en is None

    def add_en(self, data):
        x = QueueEl(data)
        x.next = None
        if self.is_empty():
            self.bg = x
        else:
            self.en.next = x
        self.en = x

    def take_bg(self):
        if self.is_empty():
            return False
        p = self.bg
        data = p.data
        if self.bg == self.en:
            self.bg = self.en = None
        else:
            self.bg = self.bg.next
        del p
        return data

    def __str__(self):
        els = ''
        if not self.is_empty():
            p = self.bg
            while p.next is not None:
                els += str(p.data) + ', '
                p = p.next
            els += str(p.data)
        return els

    def __len__(self):
        len = 0
        if not self.is_empty():
            p = self.bg
            while p.next is not None:
                len += 1
                p = p.next
            len += 1
        return len

    def __add__(self, other):
        for i in range(len(other)):
            self.add_en(other.take_bg())
        return self

    def copy(self):
        a = Queue()
        for i in range(len(self)):
            e = self.take_bg()
            a.add_en(e)
            self.add_en(e)
        return a

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)


import random

# 10.6
print('choose the mode:', '0 - easy', '1 - hard', sep = '\n')
g = int(input())
if g != 1 and g != 0:
    print('you lose')
t = int(input('set the period to wait (minutes): '))
if g == 0:
    print('\n', 'welcome to Novus')
    m = random.choice(range(3, 7))
if g == 1:
    print('\n', 'you\'re in ATB')
    m = random.choice(range(7, 13))

s = Queue()
for i in range(m):
    s.add_en(i)
print('start\n', s)

t1 = t2 = t
graph = []
while True:
    if t2 > 0:
        if g == 0:
            w = random.choice(range(4, 8))
        if g == 1:
            w = random.choice(range(4))
        s.add_en(m)
        graph.append((t - t2, '+', m))
        m += 1
        t2 -= w
    if t1 > 0:
        if g == 0:
            w = random.choice(range(3, 6))
        if g == 1:
            w = random.choice(range(1, 3))
        u = s.take_bg()
        if u >= 0:
            graph.append((t - t1, '-', u))
        t1 -= w
    if t1 <= 0 and t2 <= 0:
        break

print('finish\n', s)
print()

graph.sort()
for i in graph:
    print('{} min: {} unit {}'.format(i[0], i[1], i[2]))
print()

if 0 <= g <= 1:
    if s.is_empty():
        print('you win!')
    else:
        print('try again')
print('\n')

# 10.7
s = Queue()
l = int(input('how long queue do you want? '))
n = int(input('enter n <= {}: '.format(l)))
print('press "0" if you choose the random')
if input() == '0':
    for i in range(l):
        s.add_en(random.choice(range(21)))
else:
    for i in range(l):
        s.add_en(input('enter: '))
# a)
print('a)')
t = Queue()
r = Queue()
print(s)
while not s.is_empty():
    while len(s) != 1:
        t.add_en(s.take_bg())
    r.add_en(s.take_bg())
    s, t = t, s
s = r
print(s)
# b)
print('b)')
if n > l:
    print('not right')
else:
    for i in range(n):
        e = s.take_bg()
        print(i+1, ': ', e, sep = '')
        t.add_en(e)
    print('rest of the queue: ', s)
# c)
print('c)')
print('s: ', s)
print('t: ', t)
s1 = s.copy()
t1 = t.copy()
print('s + t: ', s1 + t1)
s1 = s.copy()
t1 = t.copy()
print('t + s: ', t1 + s1)
# d)
print('d)')
if s >= t:
    print('s >= t')
if s <= t:
    print('s <= t')


