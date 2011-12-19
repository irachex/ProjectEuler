max_num = 28124
d = [0] * max_num 
r = [0] * max_num
prime_list = []
for n in range(2, max_num):
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

a = [i for i in range(max_num) if d[i]-i>i]
f = [False] * max_num
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i]+a[j]<max_num:
            f[a[i]+a[j]] = True
        else:
            break
print sum([i for i in range(max_num) if f[i] is False])
