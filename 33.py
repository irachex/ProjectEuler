from fractions import gcd

frac, deno = 1, 1

def is_correct(a, b, c, d):
    global frac, deno
    if a*d == b*c:
        frac *= a
        deno *= b
        return True
    return False

for i in range(1, 10):
    for j in range(i+1, 10):
        for k in range(1, 10):
            is_correct(i*10+k, j*10+k, i, j) 
            is_correct(i*10+k, k*10+j, i, j)
            is_correct(k*10+i, j*10+k, i, j)
            is_correct(k*10+i, k*10+j, i, j)

print frac, deno
print deno/gcd(frac, deno)