import math
from collections import deque

limit = 1000000
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

def ok(prime_set, new_prime):
    global pairs
    for i in prime_set:
        if pairs.get((prime_list[i], new_prime), False) or \
        not is_prime_num(int(str(prime_list[i])+str(new_prime))) or \
        not is_prime_num(int(str(new_prime)+str(prime_list[i]))):
            pairs[(prime_list[i], new_prime)] = False
            return False
        else:
            pairs[(prime_list[i], new_prime)] = True
    return True

def bfs_find(dep):
    q = deque([[i] for i in range(len(prime_list))])
    while q:
        head = q.popleft()
        for i in range(head[-1]+1, len(prime_list)):
            if ok(head, prime_list[i]):
                prime_set = head+[i]
                q.append(prime_set)
                if len(prime_set)==dep:
                    print [prime_list[i] for i in prime_set],
                    print sum([prime_list[i] for i in prime_set])
                    #return

def dfs_find(dep, prime_sum, prime_set):
    global min_sum
    global min_set
    if dep==0:
        if min_sum>prime_sum:
            min_sum=prime_sum
            min_set=prime_set
            print min_sum, [prime_list[i] for i in min_set]
        return
    left = 0
    if prime_set:
        left = prime_set[-1]+1
    for i in range(left, len(prime_list)):
        if prime_sum+prime_list[i]>min_sum:
            return
        if ok(prime_set, prime_list[i]):
            dfs_find(dep-1, prime_sum+prime_list[i], prime_set+[i])
            
        
#bfs_find(5)
pairs = {}
min_sum = 30000
min_set = []
dfs_find(5, 0, [])
                


    
    
    