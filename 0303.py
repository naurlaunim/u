import random

# # 7.112
# x = int(input('enter x: '))
# f = open('mngchln.txt', 'w')
# f.write('-14 \n')
# f.write('25 \n')
# f.write('32 \n')
# f.write('53 \n')
# f = open('mngchln.txt', 'r')
# ll = f.readlines()
# l = [int(i) for i in ll]
# P = x**3*l[0] + x**2*l[1] + x*l[2] + l[3]
# print(P)
# dp = 3*x**2*l[0] + 2*x*l[1] + l[2]
# print(dp)

# # 7.113
# f = open('nmbrs.txt', 'w')
# for i in range(10):
#     k = random.choice(range(-200, 200))/random.choice([2, 4, 5])
#     f.write('{} \n'.format(k))
# f.close()
# f = open('nmbrs.txt', 'r')
# ll = f.readlines()
# l = [float(i) for i in ll]
# print(l)
# def ppfn():
#     f = open('nmbrs.txt', 'r')
#     ll = f.readlines()
#     l = [float(i) for i in ll]
#     a = sum(l)
#     bl = [i for i in l if i < 0]
#     b = len(bl)
#     c = l[-1]
#     d = max(l)
#     el = [l[i] for i in range(len(l)) if i%2 == 0]
#     e = min(el)
#     f = d + min(l)
#     g = l[1] - l[-1]
#     hl = [i for i in l if i < a/len(l)]
#     h = len(hl)
#     return {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h}
# d = ppfn()
# s = list(d.keys())
# s.sort()
# for i in s:
#     print(i + ')', d.get(i))


# 117
n = int(input('n = '))
def fib(n):
    if n <= 0:
        print('try again')
        return None
    fl = [1, 1]
    i = 2
    while i < n:
        ei = fl[-1] + fl[-2]
        fl.append(ei)
        i += 1
    return fl
f = open('fbnch.txt', 'w')
l = fib(n)
for i in range(len(l)):
    f.write('{} \n'.format(l[i]))
f.close()

# 118
f1 = open('nmbrs1.txt', 'w')
for i in range(50):
    k = random.choice(range(-100, 100))
    f1.write('{} \n'.format(k))
f1.close()
f1 = open('nmbrs1.txt', 'r')
ll = f1.readlines()
l = [int(i) for i in ll]
f1.close()

f2 = open('nmbrs2.txt', 'w')
a = [i for i in l if i%2 == 0]
f2.write('a) ' + str(a)[1:-1] + '\n')
b = [i for i in l if i%3 == 0 and i%5 == 0]
f2.write('b) ' + str(b)[1:-1] + '\n')
c = []
for i in l:
    for j in range(i//2):
        if j**2 == i:
            c.append(i)
f2.write('c) ' + str(c)[1:-1] + '\n')
d = l[::-1]
f2.write('d) ' + str(d)[1:-1] + '\n')
e = set(l)
f2.write('e) ' + str(e)[1:-1] + '\n')
f2.close()

# 119
f = open('f.txt', 'w')
for i in range(20):
    k = random.choice(range(-100, 100))
    f.write('{} \n'.format(k))
f.close()
f = open('f.txt', 'r')
g = open('g.txt', 'w')
h = open('h.txt', 'w')
for line in f:
    k = int(line)
    if k%2 == 0:
        g.write(str(k) + '\n')
    else:
        h.write(str(k) + '\n')
f.close()
g.close()
h.close()