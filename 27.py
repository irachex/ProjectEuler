prime_list = []

def isprime(n):
    if n<0: return False
    for p in prime_list:
        if n!=p and n%p == 0:
            return False
    return True
    
def cal(a, b):
    i = 0
    while True:
        if isprime(i*i+i*a+b) is True:
            i+=1
        else:
            break
    return i


for i in range(2, 1000):
    if isprime(i):
        prime_list.append(i)

max_r, max_a, max_b = 0, 0, 0
for a in range(-1000, 1000):
    for b in prime_list:
        r = cal(a, b)
        if max_r<r:
            max_r, max_a, max_b = r, a, b

print max_r
print max_a*max_b
