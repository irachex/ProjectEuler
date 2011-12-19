import math

limit = 1000000
f = {}
prime_list = []
is_prime = [False, False] + [True]*limit
n = 2
cnt = 0
while True:
    f.update({n:{}})
    if is_prime[n] is True:
        prime_list.append(n)
        f[n] = {n:1}
        for j in range(n*n, limit, n):
            is_prime[j] = False
    else:
        for p in prime_list:
            if n%p == 0:
                f[n] = dict(f[n/p])
                if p not in f[n]:
                    f[n].update({p:1})
                else:
                    f[n][p] += 1
                break
        
    if len(set(f[n])) == 4:
        cnt += 1
        if cnt == 4:
            print n-3, n-2, n-1, n
            exit()
    else:
        cnt = 0
    n += 1
    
    
