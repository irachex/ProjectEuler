limit = 1000000
prime_list = []
is_prime = [False, False] + [True]*limit
for i in range(2, limit):
    if is_prime[i] is True:
        prime_list.append(i)
        for j in range(i*i, limit, i):
            is_prime[j] = False

def count(p):
    s = str(p)
    max_cnt = 0
    for i in range(len(s)-1):
        for j in range(i+1,len(s)+1):
            cnt = 0
            for k in range(10):
                n = int(s[:i] + str(k)*(j-i) + s[j:])
                if is_prime[n]:
                    cnt += 1
            if max_cnt<cnt: max_cnt = cnt
    return max_cnt
    
print count(56003)

prime_list = prime_list[10:]
for p in prime_list:
    if count(p)>=8:
        print p
        exit()