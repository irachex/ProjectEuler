import math

limit = 100000
prime_list = []
is_prime = [False, False] + [True]*limit
for i in range(3, limit, 2):
    if is_prime[i] is True:
        prime_list.append(i)
        for j in range(i*i, limit, i):
            is_prime[j] = False

def is_prime_num(n):
    if n<limit:
        return is_prime[n]
    lim = math.sqrt(n)
    for i in prime_list:
        if n%i==0:
            return False
        if i>math.sqrt(n):
            break
    return True


total, cnt = 0, 0
num, sub = 1, 2
while total<10 or cnt >= total*0.1:
    total += 1
    if is_prime_num(num):
        cnt += 1
    #print float(cnt)/float(total)
    num += 2*((total-1)/4+1)
print ((total-1)/4+1)*2-1
        