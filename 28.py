n = 1001
x, y, d, a, acnt, s = 0, 0, 0, 1, 0, 1
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for i in range(2, n*n+1):
    x += dx[d]
    y += dy[d]
    if abs(x) == abs(y): 
        s+= i
    acnt += 1
    if acnt == a: d = (d+1)%4
    if acnt == a+a:
        d = (d+1)%4
        a += 1
        acnt = 0
print s
    