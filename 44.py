p = []
for i in range(1, 5000):
    p.append(i*(3*i-1)/2)
pset = set(p)

for i in range(len(p)):
    for j in range(i+1, len(p)):
        if p[i]+p[j] in pset and p[j]-p[i] in pset:
            print p[j]-p[i]
            exit()
       # if j<len(p)-1 and p[i]+p[j]<p[j+1] or p[i]+p[j]*2>p[-1]:
    #        break
