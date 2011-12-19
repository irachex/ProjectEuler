import math
count = [0]*1001
for a in range(1,1000):
    for b in range(a,1000-a):
        c = math.sqrt(a*a + b*b)
        if a+b+c<=1000 and abs(c-int(c))<1e-04:
            count[int(a+b+c)] += 1
max_count = 0
p = 0
for i in range(1001):
    if max_count < count[i]:
        max_count = count[i]
        p = i
print p
    
            