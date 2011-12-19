li = []
for a in range(2, 101):
    for b in range(2, 101):
        li.append(a**b)
print len(set(li))
        