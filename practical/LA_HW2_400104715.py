# help from : https://www.geeksforgeeks.org/xor-basis-algorithm/


n, m = list(map(int, input().split()))
Basis = [0] * n
def add(mask):
    for i in range(n):
        if (mask & (1 << i)):
            if (Basis[i] == 0):
                Basis[i] = mask
                print("NO")
                return
            mask ^= Basis[i]
    print("YES")
    return

for i in range(m):
    add(int(input(),2))


