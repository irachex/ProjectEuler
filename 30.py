s = 0
for i in range(10, 990999):
    if i == sum(map(lambda x:x**5,map(int,str(i)))):
        print i
        s += i
print s