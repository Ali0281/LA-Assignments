import math


def dot_prod(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))


def QRfac(A):
    m = len(A)
    Q = [[0.0] * m for _ in range(m)]
    n = len(A[0])
    R = [[0.0] * m for _ in range(m)]
    for i in range(n):
        V = [A[j][i] for j in range(m)]
        for j in range(i):
            R[j][i] = 0.0
            for k in range(m):
                R[j][i] += Q[k][j] * A[k][i]
            for k in range(m):
                V[k] -= R[j][i] * Q[k][j]
        R[i][i] = math.sqrt(dot_prod(V, V))
        for j in range(m):
            Q[j][i] = V[j] / R[i][i]
    return Q, R


def my_mult(a, b):
    n = len(a)
    res = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = dot_prod(a[i], [b[k][j] for k in range(n)])
    return res


a = []
n = int(input())
test_iter = 2200
for i in range(n):
    a.append([float(i) for i in input().split()])
for i in range(test_iter):
    Q, R = QRfac(a)
    a = my_mult(R, Q)

e_vals = [a[i][i] for i in range(len(a))]
e_vals.sort()

det = 1
for e_val in e_vals:
    det *= e_val
    print(f"{round(e_val, 3):.3f}", end="\t")
print(f"\n{round(det, 3):.3f}")
