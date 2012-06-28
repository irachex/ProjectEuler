f = open('matrix.txt')
N = 100
d = [[999999999 for j in range(N)] for i in range(N)]
d[1][0] = d[0][1] = 0
i = 1
for line in f:
    a = map(int, line.split(','))
    n = len(a)
    for j in range(1, len(a) + 1):
        d[i][j] = min(d[i - 1][j], d[i][j - 1]) + a[j - 1]
    i += 1
print d[n][n]


