def cal(d):
    r = 1
    b = [False]*1000
    i = 0
    while r!=0:
        r = (r*10)%d
        if b[r]:
            return i
        i += 1
        b[r] = True
    return 0
        
    
d = 1
max_cycle, max_d = 0, 0
while d<1000:
    r = cal(d)
    if max_cycle < r:
        max_cycle, max_d = r, d
    d += 1

print max_d