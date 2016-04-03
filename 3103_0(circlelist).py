class CL_El():
    def __init__(self, data):
        self.data = data
        self.next = None

class CircleList():
    def __init__(self):
        self.current = None

    def next(self):
        if self.current is None:
            return False
        self.current = self.current.next

    def insert(self, data):
        if self.current is None:
            element = CL_El(data)
            self.current = element.next = element
        else:
            element = CL_El(self.current.data)
            self.current.data = data
            element.next = self.current.next
            self.current.next = self.current = element

    def get(self):
        if self.current is None:
            return False
        return self.current.data

    def remove(self):
        if self.current is None:
            return False
        elif self.current.next == self.current:
            p = self.current
            self.current = None
        else:
            p = self.current.next
            self.current.data = p.data
            self.current.next = p.next
        del p
        return True

    def __len__(self):
        len = 0
        if self.current is not None:
            p = self.current
            len += 1
            self.next()
            while p != self.current:
                len += 1
                self.next()
        return len

    def __str__(self):
        s = ''
        for i in range(len(self)):
            s += str(self.get()) + ', '
            self.next()
        return s[:-2] + '.'

    def copy(self):
        s = CircleList()
        for i in range(len(self)):
            s.insert(self.get())
            self.next()
        return s

    def change(self, n):
        self.current.data = n
        return self

    def copy_el(self, n, m):
        l = CircleList()
        x = len(self) - (n+m)
        for i in range(m):
            self.next()
        for i in range(n):
            l.insert(self.get())
            self.remove()
        for i in range(x):
            self.next()
        return l

    def del_el(self, n, m):
        x = len(self) - (n+m)
        for i in range(m):
            self.next()
        for i in range(n):
            self.remove()
        for i in range(x):
            self.next()




import random

# 10.20 (classwork)
# s = CircleList()
# l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
# for i in range(random.choice(range(5, 10))):
#     s.insert(l[i])
# rhyme = ['Ten little Injuns standin\' in a line,\nOne toddled home and then there were nine;', 'Nine little Injuns swingin\' on a gate,\nOne tumbled off and then there were eight.', 'Eight little Injuns gayest under heav\'n.\nOne went to sleep and then there were seven;', 'Seven little Injuns cuttin\' up their tricks,\nOne broke his neck and then there were six.', 'Six little Injuns all alive,\nOne kicked the bucket and then there were five;', 'Five little Injuns on a cellar door,\nOne tumbled in and then there were four.', 'Four little Injuns up on a spree,\nOne got fuddled and then there were three;', 'Three little Injuns out on a canoe,\nOne tumbled overboard and then there were two.', 'Two little Injuns foolin\' with a gun,\nOne shot t\'other and then there was one;', 'One little Injun livin\' all alone,\nHe got married and then there were none.']
# for i in range(10):
#     for j in range(9):
#         s.next()
#     print(rhyme[i])
#     print('- unit', s.get())
#     s.remove()
#     if len(s) == 1:
#         break
# print('\nand the winner is:', s.get())

# # b)
# l = [i for i in range(10)]
# s = CircleList()
# for i in range(10):
#     j = l.pop(random.choice(range(len(l))))
#     s.insert(j)
# print(s)
#
# x = random.choice(range(10))
# print('x =', x)
# for i in range(len(s)):
#     if s.get() == x:
#         print('element "{}" found at the position {}'.format(x, i))
#     s.next()
#
# s1 = s.copy()
# del s
# print(s1)

# 10.21
l = [i for i in range(10)]
s = CircleList()
for i in range(10):
    j = l.pop(random.choice(range(len(l))))
    s.insert(j)
print(s)
print('a)')
s.change(int(input('n = ')))
print(s)
print('b)')
print(s)
s1 = s.copy()
print(s.copy_el(int(input('n = ')), int(input('m = '))))
print(s)
print('c)')
s = s1
print(s)
s.del_el(int(input('n = ')), int(input('m = ')))
print(s)