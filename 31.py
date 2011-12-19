a = [1,2,5,10,20,50,100,200]
n = 200
d = [([1]+[0]*n) for i in range(len(a))]
for i in range(len(a)):
    for j in range(1, n+1):
        if i>0: d[i][j] = d[i-1][j]
        if j-a[i]>=0:
            d[i][j] += d[i][j-a[i]]

print d[len(a)-1][n]