class StackEl():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.bg = None

    def is_empty(self):
        return self.bg is None

    def push(self, data):
        s = StackEl(data)
        s.next = self.bg
        self.bg = s

    def pop(self):
        if self.is_empty():
            return False
        p = self.bg
        data = p.data
        self.bg = p.next
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
        return(len)


s = Stack()
s.push(input('enter: '))
s.push(input('enter: '))
s.push(input('enter: '))
s.push(input('enter: '))
s.push(input('enter: '))
print(s)

# 10.1
v = Stack()
g = Stack()
while not s.is_empty():

    min = s.pop()
    v.push(min)
    while not s.is_empty():
        p = s.pop()
        if p < min:
            min = p
        v.push(p)

    while not v.is_empty():
        p = v.pop()
        if p == min:
            g.push(p)
        else:
            s.push(p)
while not g.is_empty():
    p = g.pop()
    s.push(p)
print('1.', s)

# 10.2 a)
print('2. a)', len(s))
# b)
while not s.is_empty():
    p = s.pop()
    g.push(p)
s = g
print('2. b)', s)