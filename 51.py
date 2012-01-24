limit = 1000000
prime_list = []
is_prime = [False, False] + [True]*limit
for i in range(2, limit):
    if is_prime[i] is True:
        prime_list.append(i)
        for j in range(i*i, limit, i):
            is_prime[j] = False

def count(p, i):
    s = str(p)
    cnt = 0
    for k in range(10):
        n = int(s.replace(str(i), str(k)))
        if is_prime[n] and len(str(n))==len(s):
            cnt += 1
    return cnt
    

prime_list = prime_list[10:]
for p in prime_list:
    for i in range(3):
        if str(i) in str(p) and count(p, i)>=8:
            print p
            exit()