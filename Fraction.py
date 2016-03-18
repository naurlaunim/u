class Fraction:

    def __init__(self, a, b):
        self.numerator = int(a)
        self.denominator = int(b)

    def __mul__(self, other):
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    # TODO __truediv__, __add__, __sub__ + magic for <, >, ==, !=, <=, >=

    def __truediv__(self, other):
        return Fraction(
            self.numerator * other.denominator,
            self.denominator * other.numerator
        )

    def __add__(self, other):
        a = self.numerator * other.denominator
        b = other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(a + b, d)

    def __sub__(self, other):
        a = self.numerator * other.denominator
        b = other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(a - b, d)



    def __lt__(self, other):
        a = self.numerator * other.denominator
        b = other.numerator * self.denominator
        if a < b:
            return True
        else:
            return False

    def __gt__(self, other):
        a = self.numerator * other.denominator
        b = other.numerator * self.denominator
        if a < b:
            return True
        else:
            return False

    def __le__(self, other):
        a = self.numerator * other.denominator
        b = other.numerator * self.denominator
        if a <= b:
            return True
        else:
            return False

    def __ge__(self, other):
        a = self.numerator * other.denominator
        b = other.numerator * self.denominator
        if a >= b:
            return True
        else:
            return False

    def __eq__(self, other):
        a = self.numerator * other.denominator
        b = other.numerator * self.denominator
        if a == b:
            return True
        else:
            return False

    def __ne__(self, other):
        a = self.numerator * other.denominator
        b = other.numerator * self.denominator
        if a != b:
            return True
        else:
            return False

    def print(self):
        print(self.numerator, '/', self.denominator)

    def reduce(self):
        # TODO: reduce fraction
        if self.numerator % self.denominator == 0:
            return self.numerator / self.denominator
        a = b = 0.1
        # print(a, b, '1')
        while a != self.denominator and b != self.denominator:
            a = self.numerator
            b = self.denominator
            for i in [2, 3, 5, 7, 11, 17, 19, 23, 27]:
                if self.numerator % i == 0 and self.denominator % i == 0:
                    self.numerator = int(self.numerator / i)
                    self.denominator = int(self.denominator / i)
        return self

    # TODO: get 0.25 from 1/4
    def to_decimal(self):
        return self.numerator / self.denominator


f1 = Fraction(3, 4)
f2 = Fraction(12, 7)

f1.print()
f2.print()

g = f1 * f2
g.reduce()
print('Multiplying: ', end = '')
g.print()

g = f1 / f2
g.reduce()
print('Division: ', end = '')
g.print()

g = f1 + f2
g.reduce()
print('Addition: ', end = '')
g.print()

g = f1 - f2
g.reduce()
print('Subtracting: ', end = '')
g.print()

print()
h = Fraction(30, 45)
k = Fraction(20, 30)
h.print()
h.reduce()
print('Reducing: ', end = '')
h.print()

print()
if h == k:
    print('{}/{} = {}/{}'.format(h.numerator, h.denominator, k.numerator, k.denominator))
if f1 != f2:
    print('{}/{} != {}/{}'.format(f1.numerator, f1.denominator, f2.numerator, f2.denominator))
if f1 < f2:
    print('{}/{} < {}/{}'.format(f1.numerator, f1.denominator, f2.numerator, f2.denominator))
if h <= k:
    print('{}/{} <= {}/{}'.format(h.numerator, h.denominator, k.numerator, k.denominator))


print()
q = Fraction(1, 4)
j = q.to_decimal()
print('{}/{} = {}'.format(q.numerator, q.denominator, j))

