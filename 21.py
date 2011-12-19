d = [0] * 10001 
r = [0] * 10001
prime_list = []
for n in range(2, 10001):
    d[n] = 0
    for p in prime_list:
        if n%p == 0:
            if (n/p)%p==0:
                d[n] = d[n/p] + r[n/p]*p
            else:
                d[n] = d[n/p] * (p+1)
            r[n] = d[n] - d[n/p]
            break
    if not d[n]:
        prime_list.append(n)
        r[n] = n
        d[n] = 1 + n

d = [d[i]-i for i in range(10001)]
print sum([n for n in range(10001) if d[n]<10001 and n == d[d[n]] and n!=d[n] ])