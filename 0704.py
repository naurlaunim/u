import random
import turtle

class BinaryTree:
    def __init__(self):
        self.data = self.ls = self.rs = None

    def is_empty(self):
        return self.data == self.ls == self.rs == None

    def make_tree(self, data, t1, t2):
        self.data = data
        self.ls = t1
        self.rs = t2

    def root(self):
        if self.is_empty():
            return 'empty'
        return self.data

    def vievdata(self):
        turtle.setheading(180)
        if self.data is None:
            turtle.circle(5)
            return
        x = self.data
        if abs(x) < 10:
            turtle.circle(10, 170)
            turtle.write(x)
            turtle.circle(10, 190)
        if 10 <= abs(x) < 1000:
            turtle.circle(10, 135)
            turtle.write(x)
            turtle.circle(10, 225)
        if abs(x) >= 1000:
            turtle.circle(5)
            turtle.write(x)


    def vievtree(self, r = 50, k = 2/3):
        self.vievdata()
        if self.is_empty():
            return
        turtle.setheading(-90)
        turtle.up()
        turtle.forward(20)
        turtle.down()
        turtle.setheading(-135)
        turtle.forward(r)
        self.ls.vievtree(r*k, k)
        turtle.setheading(45)
        turtle.forward(r)
        turtle.right(90)
        turtle.forward(r)
        self.rs.vievtree(r*k, k)
        turtle.setheading(135)
        turtle.forward(r)
        turtle.setheading(90)
        turtle.up()
        turtle.forward(20)
        turtle.down()



def bitree(t, a, b, ep):
    if abs(b-a) < ep:
        return
    i = int(abs(b-a)/3)
    c = random.choice(range(a + i, b+1 - i))
    tl = BinaryTree()
    tr = BinaryTree()
    t.make_tree(c, tl, tr)
    bitree(tl, a, c, ep)
    bitree(tr, c+1, b, ep)

turtle.width(2)
turtle.color('#33cccc')
t = BinaryTree()
bitree(t, 0, 50, 5)
turtle.up()
turtle.goto(0, 200)
turtle.down()
t.vievtree(100, 1/2)


def find(t0, t, x):
    t1 = BinaryTree()
    if x == t.data:
        t0.make_tree(t.data, BinaryTree(), BinaryTree())
        return
    if x < t.data:
        t1.data = t.ls.data
        t0.data = t.data
        t0.ls = t1
        t0.rs = BinaryTree()
        t0.rs.data = t0.rs.ls = t0.rs.rs = None
        if t.ls.is_empty():
            return
        find(t1, t.ls, x)
    if t.data < x:
        t1.data = t.rs.data
        t0.data = t.data
        t0.ls = BinaryTree()
        t0.ls.data = t0.ls.ls = t0.ls.rs = None
        t0.rs = t1
        if t.rs.is_empty():
            return
        find(t1, t.rs, x)

tf = BinaryTree()
find(tf, t, 21)
turtle.up()
turtle.goto(0, 200)
turtle.down()
turtle.color('#ff66ff')
tf.vievtree(100, 1/2)


turtle.up()
turtle.goto(0, -200)
turtle.mainloop()
