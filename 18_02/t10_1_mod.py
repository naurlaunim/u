# 1)
def mx():
    A = []
    n = int(input('the number of rows: '))
    m = int(input('the number of columns: '))
    for i in range(n):
        A.append([])
        for j in range(m):
            print('element', i, j)
            x = float(input())
            A[i].append(x)
    return A

def mx_rndm():
    import random
    A = []
    n = int(input('the number of rows/columns: '))
    rng = int(input('range: '))
    for i in range(n):
        A.append([])
        for j in range(n):
            x = random.choice(range(rng))
            A[i].append(x)
    return A

# 2)
def prnt(A):
    print(*A, sep = '\n')

# 3)
def mul(a, b):
    A = [k for k in a] # 'cause my pycharm can not into
    B = [l for l in b]
    if len(A[0]) == len(B):
        m = len(A)
        n = len(B)
        k = len(B[0])
    else:
        return None
    C = []
    for i in range(m):
        p = []
        for j in range(k):
            q = 0
            for f in range(n):
                q += A[i][f]*B[f][j]
            q = round(q, 3)
            p.append(q)
        C.append(p)
    return C
    '''  matrix multiplication '''

# 4), 5)
def vct_right(a, b):
    from t10_1_mod import mul
    if len(a[0]) != len(b):
        return 'invalid move'
    B = []
    for i in b:
        l = []
        l.append(i)
        B.append(l)
    r = mul(a, B)
    r = [o[0] for o in r]
    return r

def vct_left(b, a):
    from t10_1_mod import mul
    if len(b) != len(a):
        return 'invalid move'
    B = []
    B.append(b)
    r = mul(B, a)
    return r[0]

# 6), 7)
def el_p(i, j, n):
    A = []
    for u in range(n):
        l = [0 for v in range(n)]
        l[u] = 1
        A.append(l)
    A[i][j], A[i][i] = A[i][i], A[i][j]
    A[j][i], A[j][j] = A[j][j], A[j][i]
    return A

def chng_r(r1, r2, a):
    from t10_1_mod import el_p, mul
    return mul(el_p(r1, r2, len(a)), a)

def chng_c(c1, c2, a):
    from t10_1_mod import el_p, mul
    return mul(a, el_p(c1, c2, len(a[0])))

# 8)
def gettherow(i, a): # very strange task 1
    row = a[i]
    return row

# 9)
def skalar_mul(v, k):
    V = [i*k for i in v]
    return V

# 10)
def strangetask2(a, v):
    if len(v) != len(a[0]):
        return 'invalid move'
    A = []
    for i in a:
        A.append([i[j]-v[j] for j in range(len(i))])
    return A


