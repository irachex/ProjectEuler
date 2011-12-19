def base2(n):
    s = ""
    while n>0:
        s += str(n%2)
        n /= 2
    return s

s = 0
for i in range(1000000):
    if str(i) == str(i)[::-1]:
        b = base2(i)
        if b == b[::-1]:
            s += i
print s
            