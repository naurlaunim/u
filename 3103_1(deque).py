class DequeEl():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque():
    def __init__(self):
        self.bg = self.en = None

    def is_empty(self):
        return self.bg is self.en is None

    def put_en(self, data):
        x = DequeEl(data)
        if self.is_empty():
            self.bg = self.en = x
        else:
            self.en.next = x
            x.prev = self.en
        self.en = x

    def put_bg(self, data):
        x = DequeEl(data)
        if self.is_empty():
            self.bg = self.en = x
        else:
            self.bg.prev = x
            x.next = self.bg
        self.bg = x

    def get_bg(self):
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

    def get_en(self):
        if self.is_empty():
            return False
        p = self.en
        data = p.data
        if self.bg == self.en:
            self.bg = self.en = None
        else:
            self.en = self.en.prev
        del p
        return data

    def __del__(self):
        while self.bg is not None:
            p = self.bg
            self.bg = self.bg.next
            del p
        self.en = None

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
        s1 = Deque()
        for i in range(len(self)):
            x = self.get_bg()
            s1.put_en(x)
            self.put_en(x)
        for i in range(len(other)):
            x = other.get_bg()
            s1.put_en(x)
            other.put_en(x)
        return s1

import random
# 10.12
d = Deque()
for i in range(int(input('m = '))):
    if i%2 == 0:
        d.put_bg(random.choice(range(10)))
    else:
        d.put_en(random.choice(range(10)))
print(d)

for i in range(int(input('n = '))):
    x = random.choice([0, 1, 2, 3])
    if x == 0:
        print(d.get_bg())
    if x == 1:
        d.put_en(int(input('input: ')))
    if x == 2:
        print(d.get_en())
    if x == 3:
        d.put_en(int(input('input: ')))
print(d)

# 10.14 b)
d1 = Deque()
for i in range(4):
    if i%2 == 0:
        d1.put_bg(random.choice(range(10)))
    else:
        d1.put_en(random.choice(range(10)))
print(d1)
d2 = Deque()
for i in range(6):
    if i%2 == 0:
        d2.put_bg(random.choice(range(10)))
    else:
        d2.put_en(random.choice(range(10)))
print(d2)
print(d1 + d2)
print(d2 + d1)