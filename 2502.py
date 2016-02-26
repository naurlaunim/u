import random
# a = {random.choice(range(-100, 100)), random.choice(range(-100, 100)), random.choice(range(-100, 100)), random.choice(range(-100, 100)), random.choice(range(-100, 100))}
# print(a)
#
# # 7.2
# min = min(a)
# print(min)
#
# # 7.3
# l = list(a)
# l.sort()
# print(*l)
#
# # 7.4
# a.add(random.choice([random.choice(range(100, 500)), random.choice(range(-500, -100))]))
# print(a)
#
# # 7.5
# t=0
# for i in a:
#     t+=abs(i)
# print(t)
#
# #7.6
# max=max(a)
# print(abs(max-min))
#
# def srt(a):
#     r=[]
#     for i in a:
#         if i==min(a):
#             a.discard(i)
#             r.append(i)
#             return srt(a)
#         return r
# print(srt(a))

print('\n', '7.8')
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = ''
for i in range(random.choice(range(1, 9))):
    c = random.choice(l)
    n += str(c)
while n[0] == '0':
    n = n[1:]
print(n)
s = set(n)
print('a) ', s, len(s))
ls = list(set(l) - {int(i) for i in s})
ls.sort()
print('b) ', *ls)

print('\n', '7.10')
def strangefunktion(s):
    g = set(s)
    d = {i for i in g if i.isdigit()}
    o = {i for i in g if i in ['+', '-', '*', '/', '^']}
    return len(d) + len(o)
s1 = input('string: ')
print(strangefunktion(s1))

print('\n', '7.11')
s = set('qwertyuiopasdfghjklzxcvbnm')
# l = list(s)
# l.sort()
ii = ''
r = ii.join(s)
l = ''
for i in range(50):
    l += r[random.choice(range(26))]*random.choice(range(0, 3)) + r[random.choice(range(26))]
print('random string:')
print(l)

f = set(l)
v = {}
for i in f:
    p = l.find(i)
    v[p] = i
h = [i for i in v.keys()]
h.sort()
t = [(i, v[i]) for i in h]
print('a)', t)
one = []
more = []
for i in f:
    if l.count(i) == 1:
        one.append(i)
    else:
        more.append(i)
print('b) ', more)
print('c) ', one)

print('\n', '7.12')
print('i can not into cyrillic, so here will be no ukrainian vowels. sorry.')
alf = ['a', 'e', 'i', 'o', 'u', 'y']
s = set('qwertyuiopasdfghjklzxcvbnm')
ii = ''
r = ii.join(s)
l = ''
for i in range(20):
    l += r[random.choice(range(26))]*random.choice(range(0, 3)) + r[random.choice(range(26))]
print('random string again:')
print(l)
r = {i for i in l if i in alf}
rl = [i for i in r]
rl.sort()
print(rl)

print('\n', '7.77')
assortment = set('qwertyuiopasdfghjklzxcvbnm')
l = list(assortment)
l.sort()
stores = []
for i in range(3):
    s = set()
    for j in range(random.choice(range(10, 20))):
        x = random.choice(l)
        s.add(x)
    stores.append(s)
print(stores)
all = assortment.copy()
any = set()
for i in stores:
    all = i & all
    any = any | i
noone = assortment - any
print('a)', all)
print('b)', any)
print('c)', noone)
