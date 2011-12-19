
limit = 1000000
b = [True] * limit
b[0], b[1] = False, False
prime_list = []
for i in range(2, limit):
    if b[i] is True:
        prime_list.append(i)
        for j in range(i*i, limit, i):
            b[j] = False

def is_trunc_prime(p):
    if p<10: return False
    s = str(p)
    for i in range(len(s)):
        if b[int(s[i:])] is False or i>0 and b[int(s[:i])] is False:
            return False
    return True

        
cnt, s = 0, 0
for p in prime_list:
    if is_trunc_prime(p):
        cnt += 1
        s += p
print cnt
print s