import math

n = 10
f = [True]*10
primes = [2, 3, 5, 7, 11, 13, 17]
ans = 0

def perm(i, s):
    global ans
    if i>4:
        if (s%1000)%primes[i-5]!=0: return
    if i>n:
        ans += s 
    for j in range(n):
        if f[j] is True:
            f[j] = False
            perm(i+1, s*10+j)
            f[j] = True
                

perm(1, 0)    
print ans            
            
