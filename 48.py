s = 0
for i in range(1, 1001):
    s += int(str(i**i)[-10:])

print str(s)[-10:]
    