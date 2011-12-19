n = 20

d = [[1]*(n+1)]*(n+1)

for i in range(1, n+1):
    for j in range(1, n+1):
        d[i][j] = d[i-1][j] + d[i][j-1]

print d[n][n]