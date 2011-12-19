import os

tri_num = set([i*(i+1)/2 for i in range(100)])
cnt = 0
words = open("42.txt").read().strip("\"").split("\",\"")
for word in words:
    if sum(map(lambda c: ord(c)-64, word)) in tri_num: cnt += 1
    print word, sum(map(lambda c: ord(c)-64, word))

print cnt
        
