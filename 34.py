fact = [0]*10
fact[0] = 1
for i in range(1, 10):
    fact[i] = fact[i-1] * i
print sum([i for i in range(10, 1000000) if i == sum(map(lambda x:fact[x],map(int,str(i))))])