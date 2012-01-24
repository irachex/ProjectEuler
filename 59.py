import os
import re
import string

#common_re = re.compile(r"the|^[^+\[$&<@#{]*$")
text = map(int, open("cipher1.txt").read().split(","))
for a in range(ord("a"), ord("z")+1):
    for b in range(ord("a"), ord("z")+1):
        for c in range(ord("a"), ord("z")+1):
            key = [a, b, c]
            s = ""
            for i in range(len(text)):
                s += chr(text[i]^key[i%3])
            if " the " in s and " a " in s and " and " in s:#common_re.match(s):
                print s
                print chr(a)+chr(b)+chr(c)
                print sum(map(ord, s))
            
