lines = sorted(open("22.txt").read().strip("\"").split("\",\""))
print sum([(i+1)*sum([ord(c)-64 for c in lines[i]]) for i in range(len(lines))])

