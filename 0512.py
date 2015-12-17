# 7.136
import random
students={}
vidm = []
borg = []
s = ['Raspberrie', 'Strawberry', 'Blackberry', 'Blueberrie', 'Orange', 'Banana', 'Mandarine', 'Pineapple', 'Apple', 'Grapefruit', 'Grapes', 'Barberry', 'Passionfruit', 'Pamela', 'Kiwi', 'Pear', 'Pumpkin', 'Melon', 'Cherry']
for i in range(100):
    a = random.choice(s)
    b = random.choice(['Fedya', 'Petya', 'Zhenya', 'Senya', 'Sasha', 'Vitya', 'Misha', 'Alex', 'Denis', 'Kolya', 'Bogdan', 'Yura', 'Andriy', 'Timur', 'Daniil', 'Kirill', 'Yegor', 'Zhora', 'Vadim', 'Slavik'])
    c = random.choice([5, 6, 7, 8, 9, 10, 11])
    d = random.choice(['A', 'B', 'C'])
    math = random.choice([1, 2, 3, 4, 5])
    phys = random.choice([2, 3, 4, 5]) #the Physics teacher is a kind man
    eng = random.choice([3, 4, 5]) #everybody knows English well
    student = (a,b,c,d)
    id = random.choice(range(500,1000))
    students[id] = [student, math, phys, eng]
    #print(id, students.get(id))
    if math >= 4 and phys >= 4 and eng >= 4:
        vidm.append([student, math, phys, eng])
    if math <= 2 and phys > 2:
        borg.append([student, 'math'])
    if phys <= 2:
        if math > 2:
            borg.append([student, 'phys'])
        if math <= 2:
            borg.append([student, 'math', 'phys'])
print('quantity of good schoolboys: ', len(vidm))
print('good schoolboys: ')
print(*vidm, sep = '\n')
print('bad schoolboys: ')
print(*borg, sep = '\n')

#  T.8.1
eng = {'raspberrie': 'malyna', 'strawberry': ['polunycya', 'clubnika'], 'blackberry': ['ozhyna', 'yezhevika', 'chorna smorodyna', 'smorodyna'], 'blueberrie': 'chornycya', 'orange': 'apel\'syn', 'banana': 'banan', 'mandarine': 'mandaryn', 'pineapple': 'ananas', 'apple': ['yablyko', 'yabko'], 'grapefruit': 'greypfrut', 'grapes': 'vynograd', 'barberry': 'barbarys', 'passionfruit': 'marakuya', 'pamela': 'pamela', 'kiwi': 'kiwi', 'pear': 'grusha', 'pumpkin': ['garbuz', 'tykva'], 'melon': 'dynya', 'cherry': 'vyshnya', 'currant': 'smorodyna', 'black currant': ['chorna smorodyna', 'smorodyna'], 'red currant': ['chervona smorodyna', 'porichka', 'smorodyna']}
ukr = {}
for k, v in eng.items():
    if list(v) == v:
        for i in v:
            if ukr.get(i) == None:
                ukr[i] = k
            else:
                if ukr.get(i) == list(ukr.get(i)):
                    s = ukr.get(i)
                    s.append(k)
                    ukr[i] = s
                else:
                    ukr[i] = [ukr.get(i), k]
    else:
        if ukr.get(v) == None:
                ukr[v] = k
        else:
            if ukr.get(v) == list(ukr.get(v)):
                s = ukr.get(v)
                s.append(k)
                ukr[v] = s
            else:
                ukr[v] = [ukr.get(v), k]
for i in ukr.keys():
    print(i, '-', ukr.get(i))

# T.8.2
import random
m = {}
n = random.choice(range(6))
for i in range(n):
    a = (random.choice(range(4)), random.choice(range(4)))
    m[a] = random.choice(range(10))
print(m)
#e
print('matrycya nyzhnye-trykutna?')
t = 'yes'
for i in m.keys():
    if i[1] > i[0]:
        t = 'no'
        break
print(t)
#je
print('matrycya diagonal\'na?')
d = 'yes'
for i in m.keys():
    if i[0] != i[1]:
        d = 'no'
        break
print(d)
#zh
print('transponovana matrycya:')
mt = {}
for i in m.keys():
    s = (i[1], i[0])
    mt[s] = m.get(i)
print(mt)

# T.8.4
import random
s = [random.choice(range(6)), random.choice(range(8)), random.choice(range(10))]
k = s.copy()
k.sort()
print(s)
if all(s[i] == k[i] for i in range(len(s))):
    print('yes')
else:
    print('no')

