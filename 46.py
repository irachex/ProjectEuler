import math

limit = 1000000
prime_list = []
is_prime = [False, False] + [True]*limit
for i in range(3, limit, 2):
    if is_prime[i] is True:
        prime_list.append(i)
        for j in range(i*i, limit, i):
            is_prime[j] = False
    else:
        flag = True
        for j in range(1, len(prime_list)):
            k = math.sqrt((i-prime_list[j])/2)
            if abs(k-int(k))<1e-4:
                flag = False
                break
        if flag:
            print i
            exit()