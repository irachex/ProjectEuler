limit = 1000000
prime_list = []
is_prime = [False, False] + [True]*limit
for i in range(2, limit):
    if is_prime[i] is True:
        prime_list.append(i)
        for j in range(i*i, limit, i):
            is_prime[j] = False
n = len(prime_list)
s = [0]*(n+1)
for i in range(1, n):
    s[i] = s[i-1] + prime_list[i-1]
for i in reversed(range(1, n+1)):
    for j in range(n-i):
        if s[i+j]-s[j]>=limit: break
        if is_prime[s[i+j] - s[j]] is True:
            print s[i+j]-s[j], i
            exit()
    