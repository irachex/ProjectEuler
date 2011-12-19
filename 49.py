limit = 10000
prime_list = []
is_prime = [False, False] + [True]*limit
for i in range(3, limit, 2):
    if is_prime[i] is True:
        prime_list.append(i)
        for j in range(i*i, limit, i):
            is_prime[j] = False
    
plist = [p for p in prime_list if p>1000]
for i in range(len(plist)):
    for j in range(i+1, len(plist)):
        c = plist[j] + plist[j] - plist[i]
        if c > 10000: break
        if is_prime[c] and sorted(str(plist[i]))==sorted(str(plist[j])) and sorted(str(plist[j]))==sorted(str(c)):
            print "%d%d%d" % (plist[i], plist[j], c)
            
            
            
    
