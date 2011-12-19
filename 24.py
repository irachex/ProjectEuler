n = 10
fact = [0]*n
fact[0] = 1
for i in range(1,n):
    fact[i] = fact[i-1]*i

a = [0]*n
b = [True]*n

def cal(i, order):
    if i == n:
        return "".join(map(str,a))
    k = 0
    for j in range(n):
        if b[j] is True:
            k += 1
            if k*fact[n-i-1] >= order:
                a[i] = j
                b[j] = False
                return cal(i+1, order - (k-1)*fact[n-i-1])
    return -1


print cal(0, 1000000)
