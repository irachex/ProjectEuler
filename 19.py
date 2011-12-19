def days(y, m):
    if m in [1,3,5,7,8,10,12]:
        return 31
    if m in [4,6,9,11]:
        return 30
    if y%400==0 or y%4==0 and y%100!=0:
        return 29
    else:
        return 28

y, m, d, w = 1900, 1, 1, 1
s = 0
while y<2001:
    if w==0 and d==1 and y>=1901: s += 1
    d += 1
    if d > days(y, m):
        d = 1
        m += 1
        if m>12:
            y += 1
            m = 1
    w += 1
    if w>6: w = 0
   # print y, m, d, w

print s
