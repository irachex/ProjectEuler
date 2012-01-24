def is_lychrel(n):
    cnt = 0
    while cnt<=50:
        n = n + int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
        cnt += 1
    return True
    
ans = 0
for i in range(10000):
    if is_lychrel(i):
        ans += 1

print ans
        
    