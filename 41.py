import math

def perm(items, n=None):
    if n is None:
        n = len(items)
    for i in range(len(items)):
        v = items[i:i+1]
        if n == 1:
            yield v
        else:
            rest = items[:i] + items[i+1:]
            for p in perm(rest, n-1):
                yield v + p

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return True
        

for i in reversed(range(10)):
    a = perm('987654321'[9-i:])
    s = set([])
    for n in a:
        if is_prime(int(n)):
            print n
            exit()
                
            
