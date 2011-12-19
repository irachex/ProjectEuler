def ok(x):
    s = sorted(str(x))
    for i in range(2, 7):
        if sorted(str(i*x)) != s:
            return False
    return True

x = 100
while not ok(x):
    x += 1
print x