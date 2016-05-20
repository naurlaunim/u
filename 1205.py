# import random
#
# # 17.1
# def strangefunction(f):
#     def strf():
#         a = f()
#         if a > 0:
#             return a
#         else:
#             return abs(a) + 500
#     return strf
#
# @strangefunction
# def gen():
#     return random.choice(range(-200, 200))
#
# for i in range(10):
#     print(i, gen())
#
#
#
# # 17.2
# def ab(a, b):
#     def _ab(f):
#         def __ab():
#             x = f()
#             if x >= a and x<=b:
#                 return x
#             else:
#                 if x<a:
#                     return a
#                 if x>b:
#                     return b
#         return __ab
#     return _ab
#
# @ab(-100, 100)
# def gen():
#     return random.choice(range(-200, 200))
#
# for i in range(10):
#     print(i, gen())
#
# ## 17.4
# def ass(f):
#     def _as(*args):
#         assert all(type(i) == str for i in args)
#         l = f(*args)
#         return l
#     return _as
#
# @ass
# def red(*args):
#     s = {i for i in args}
#     return list(s)
#
# try:
#     print(red('aaa', 'bbb', 'fff', 'ggg', 'fff'))
#     print(red('aaa', 'jjj', 4, 61))
# except AssertionError:
#     print('try again')

# 17.3
def arkw(f):
    def _arkw(*args, **kwargs):
        assert len(args) == len(kwargs)
        r = f(*args, **kwargs)
        return r
    return _arkw

@arkw
def f0(*args, **kwargs):
    r = 1
    l = list(kwargs.values())
    for i in range(min(len(args), len(kwargs))):
        s = args[i] + 1/l[i]
        r *= s
    return r

try:
    print(f0(1/2, 2/3, i = 2, j = 3))
    print(f0(1/2, 2/3, 3/4, i = 2, j = 3))
except AssertionError:
    print('try again')

# 17.5
def ss(a):
    def _ss(f):
        def __ss(*args):
            assert all(type(i) == a for i in args)
            x = f(*args)
            return x
        return __ss
    return _ss

@ss(int)
def sa(*args):
    return sum(args)/len(args)

try:
    print(sa(1, 4, 8, 8))
    print(sa(1, 4, 'a', 'b', 'c'))
except AssertionError:
    print('try again')

# 17.6
def rgs(f):
    def _rgs(*args, **kwargs):
        assert len(kwargs) == 0
        r = f(*args)
        return r
    return _rgs

@rgs
def f1(*args, **kwargs):
    l = list(args) + list(kwargs.values())
    if max(l) > sum(l):
        res = 1
    else:
        l1 = [i for i in l if i > 0]
        res = sum(l1)
    return res

try:
    print(f1(1, 1, 5, -3))
    print(f1(1, 1, 5, -1))
    print(f1(1, 1, 3, i = 5, j = -5))
except AssertionError:
    print('try again')

