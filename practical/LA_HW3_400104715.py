import numpy as np

def np_array_input():
    return np.array(list(map(int , input().split())))
def TA_round(x):
    x[np.abs(x) < 0.000001] = 0 
    return np.round(x,2)
# source : https://github.com/LuckysonKhaidem/Gauss-Jordan-Matrix-Inversion/blob/master/matrix_inversion.py
def invertor(matrix):
    M = np.array(matrix)
    size = [0] * 2
    size[0] ,size[1] = M.shape
    if size[0] != size[1] : return None
    aug_M = np.c_[M ,np.eye(size[0])]
    j = 0
    for i in range(size[0] - 1):
        piv = aug_M[i][j]
        if np.round(piv ,7) == 0:
            flag = False
            for k in range(i + 1 ,size[0]):
                if np.round(aug_M[k][j] ,7) != 0:
                    aug_M[i] , aug_M[k] = aug_M[k] , aug_M[i]
                    flag = True
                    break
            if not flag : return None
            piv  = aug_M[i][j]
        for k in range(i+1 , size[0]):
            t = aug_M[k][j]
            mul = t / piv
            aug_M[k] -= mul * aug_M[i]
        j += 1
    j = size[0] - 1
    for i in range(size[0] - 1 , 0 ,-1):
        piv = aug_M[i][j]
        if np.isclose(piv ,0): return None
        for k in range(i - 1 ,-1 ,-1):
            t = aug_M[k][j]
            mul = t / piv
            aug_M[k] -= mul * aug_M[i]
        j -= 1
    for i in range(size[0]):
        aug_M[i] /= aug_M[i][i]
    return aug_M[: , size[0]:]

m  = int(input())
n  = int(input())
p  = int(input())
x_matrix  ,y_matrix ,quary = [] ,[] ,[]
for i in range(m):
    x_matrix.append(np_array_input())
    for j in range(n-1) : input()
    y_matrix.append(np_array_input())
for i in range(p):
    quary.append(np_array_input())

x_transpose_matrix  =  np.array(x_matrix).T
y_transpose_matrix  =  np.array(y_matrix).T
invert  = invertor(x_transpose_matrix@x_transpose_matrix.T)
if invert is None : 
    print("The results are unknown")
    quit()
transformation = y_transpose_matrix@x_transpose_matrix.T@invert
# from helper code : 
if np.sum(np.abs(transformation@x_transpose_matrix - y_transpose_matrix)) > 0.01 : 
    print("The results are noisy")
for i in range(p):
    print(' '.join(list(map(str ,TA_round(transformation @ quary[i])))))
