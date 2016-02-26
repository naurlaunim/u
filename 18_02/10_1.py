from t10_1_mod import mx_rndm, prnt, chng_c, chng_r, skalar_mul, gettherow

# import random
A = mx_rndm()

prnt(A)

m = len(A)
n = m # sorry, I'll not rewrite all of this
for j in range(n):
    if A[j][j] != 1:
        for i in range(j+1, m):
            if A[i][j] == 1:
                A = chng_r(i, j, A)
                break
    if A[j][j] != 1:
        for i in range(j+1, n):
            if A[j][i] == 1:
                A = chng_c(i, j, A)

    if all(A[j][o] == 0 for o in range(n)):
        if j == m - 1:
            break
        A = chng_r(-1, j, A)
    if A[j][j] == 0:
        for i in range(j+1, m):
            if A[i][j] != 0:
                A = chng_r(i, j, A)
                break

    if all(A[o][j] == 0 for o in range(m)):
        if j == n - 1:
            break
        A = chng_r(-1, j, A)
    if A[j][j] == 0:
        for i in range(j+1, n):
            if A[j][i] != 0:
                A = chng_c(i, j, A)

    for i in range(j+1, m):
        if A[i][j] != 0:
            l = gettherow(j, A)
            l = skalar_mul(l, (A[i][j]/A[j][j]))
            A[i] = [A[i][p] - l[p] for p in range(n)]
            A[i] = [round(A[i][p], 3) for p in range(n)]

print('a)')
prnt(A)


if all(A[j][j] != 0 for j in range(n)):
    rank = n
else:
    for i in range(n):
        if A[i][i] == 0:
            rank = i
            break
print('b)', '\n', 'rank = ', rank)

print('c) det')

if m != rank:
    print('0')
else:
    det = 1
    for i in range(m):
        det *= A[i][i]
    print(det)

print('d) inverse matrix')
if m != n != rank:
    print('try again')
else:
    for i in range(n):
        l = [0 for j in range(n)]
        l[i] = 1
        A[i] = A[i] + l

    for j in range(m):
        if A[j][j] != 1:
            for i in range(j+1, m):
                if A[i][j] == 1:
                    A[i], A[j] = A[j], A[i]
                    break
        for i in range(j+1, m):
            if A[i][j] != 0:
                l = gettherow(j, A)
                l = skalar_mul(l, (A[i][j]/A[j][j]))
                A[i] = [A[i][p] - l[p] for p in range(n)]

    for h in range(m):
        j = m - h - 1
        A[j] = [o/A[j][j] for o in A[j]]
        for i in range(0, j):
            l = [o*A[i][j] for o in A[j]]
            A[i] = [A[i][p] - l[p] for p in range(len(l))]
    B = []
    for i in range(m):
        l = [round(A[i][j], 3) for j in range(n, 2*n)]
        B.append(l)

prnt(B)

