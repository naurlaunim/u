class Person:
    def __init__(self):
        self.name = None
        self.byear = None

    def input(self):
        self.name = input('surname: ')
        self.byear = input('year og birth: ')

    def print(self):
        print(self.name, self.byear, sep = '\n')

# 13.1
ph = open('phonelist.txt', 'w')
class Mate(Person):
    def input(self):
        Person.input(self)
        self.phone = input('phone number: ')
        ph = open('phonelist.txt', 'r+')
        ph.write('{}: {}'.format(self.name, self.phone))
        ph.close()

    def print(self):
        Person.print(self)
        print(self.phone)

    def find(nm):
        ph = open('phonelist.txt', 'r')
        for line in ph:
            if nm in line:
                print(line)

    def reset(nm, nmb):
        ph = open('phonelist.txt', 'r+')
        l = ph.readlines()
        ph.close()
        for i in range(len(l)):
            line = l[i]
            j = line.find(':')
            name = line[:j]
            if name == nm:
                l[i] = nm + ': ' + nmb + '\n'
        l = set(l)
        l = list(l)
        ph = open('phonelist.txt', 'w')
        ph.writelines(l)
        ph.close()


import pickle

# 13.2
tab = open('tabel.db', 'wb')
tabel = {}
pickle.dump(tabel, tab)
tab.close()
class Employee(Person):
    def __init__(self):
        Person.input(self)
        self.tabel_number = int(input('tabel number: '))
        self.salary = int(input('salary for hour: '))

    default_hours = 75

    def input(self, n):
        ds = self.salary * Employee.default_hours
        tab = open('tabel.db', 'r+b')
        tabel = pickle.load(tab)
        tab.close()
        # print(tabel)
        tabel[self.tabel_number] = (self.salary, ds, self.salary*n)
        # print(tabel)
        tab = open('tabel.db', 'r+b')
        pickle.dump(tabel, tab)
        tab.close()


    def print(self):
        Person.print(self)
        print('number: ', self.tabel_number)
        print('salary: ', self.salary)
        tab = open('tabel.db', 'r+b')
        tabel = pickle.load(tab)
        tab.close()
        print('defoult mouth salary: ', tabel.get(self.tabel_number)[1])
        print('actual mouth salary: ', tabel.get(self.tabel_number)[2])

    def printall():
        tab = open('tabel.db', 'r+b')
        tabel = pickle.load(tab)
        tab.close()
        for i in tabel.keys():
            print('number: ', i)
            print('salary: ', tabel.get(i)[0])
            print('defoult mouth salary: ', tabel.get(i)[1])
            print('actual mouth salary: ', tabel.get(i)[2])

# 13.3
class RoomType():
    def __init__(self):
        self.type_name = None
        self.payment = None

lux = RoomType()
lux.type_name = 'lux'
lux.payment = 500

st = RoomType()
st.type_name = 'standard'
st.payment = 300

ec = RoomType()
ec.type_name = 'econom'
ec.payment = 200

roomlist = []
for i in range(1,11):
    roomlist.append((i, ec))
for i in range(11,51):
    roomlist.append((i, st))
for i in range(51,66):
    roomlist.append((i, lux))
rl = open('roomlist.db', 'wb')
pickle.dump(roomlist, rl)
rl.close()

guestlist = []
gl = open('guestlist.db', 'wb')
pickle.dump(guestlist, gl)
gl.close()

class Guest(Person):
    def __init__(self):
        Person.input(self)
        self.room = int(input('room: '))
        self.term = int(input('term: '))
        rl = open('roomlist.db', 'r+b')
        roomlist = pickle.load(rl)
        rl.close()
        for i in roomlist:
            if i[0] == self.room:
                pm = i[1].payment
        inf = (self.name, self.room, self.term, pm)
        gl = open('guestlist.db', 'r+b')
        guestlist = pickle.load(gl)
        gl.close()
        guestlist.append(inf)
        gl = open('guestlist.db', 'wb')
        pickle.dump(guestlist, gl)
        gl.close()

    def seek(n):
        gl = open('guestlist.db', 'r+b')
        guestlist = pickle.load(gl)
        gl.close()
        for i in range(len(guestlist)):
            if guestlist[i][0] == n or guestlist[i][1] == n:
                Output.prnt(guestlist[i])

    def printall():
        gl = open('guestlist.db', 'r+b')
        guestlist = pickle.load(gl)
        gl.close()
        for i in guestlist:
            Output.prnt(i)

class Output():
    def prnt(item):
        print('name: ', item[0])
        print('room: ', item[1])
        print('term: ', item[2])
        print('to pay: ', item[3])

# 13.4
ways = [('A', 'B', 300), ('B', 'C', 455), ('A', 'C', 340), ('B', 'D', 710)]
users = [('A', 'C'), ('B', 'C')]

class Passenger(Person):
    def __init__(self):
        Person.input(self)
        self.out = input('Departure: ')
        self.to = input('Arrival: ')
        users.append((self.out, self.to))



    def all():
        km = 70
        for i in users:
            print(i[0], '-', i[1])
            for j in ways:
                if i[0] == j[0] and i[1] == j[1]:
                    print(j[2], 'km')
                    print('cost: ', j[2]*km)

Passenger.all()