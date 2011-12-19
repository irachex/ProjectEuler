f = [1] + [0]*100
for i in range(1, 101):
    f[i] = f[i-1] * i

def count(n):
    cnt = 0
    for i in range(n):
        if f[n]/(f[i]*f[n-i]) > 1000000:
            return n+1-i*2
    return 0
    
print sum([count(n) for n in range(101)])