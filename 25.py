a = 1
b = 1
c = 0
i = 2
while len(str(b))<1000:
    c = a + b
    a = b
    b = c
    i += 1
print i