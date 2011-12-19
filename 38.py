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

def is_concat(n, i):
    x = int(n[:i])
    cnt = 1
    k = i
    while i<9:
        cnt += 1
        if n.find(str(x*cnt)) == i:
            i += len(str(x*cnt))
        else:
            return False
    return True

a = perm('987654321')
s = set([])
for n in a:
    for i in range(1, 8):
        if is_concat(n, i):
            print n, n[:i]
            exit()
                
            
