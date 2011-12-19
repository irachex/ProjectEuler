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

a = perm('123456789')
s = set([])
for n in a:
    for i in range(1, 8):
        for j in range(i+1, 9):
            if int(n[:i]) * int(n[i:j]) == int(n[j:]):
                #print int(n[:i]), int(n[i:j]), int(n[j:])
                s = s | set([int(n[j:])])
print s
print sum(s)
                
            
        