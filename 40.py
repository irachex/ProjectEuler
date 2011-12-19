length, i, f, s = 0, 0, 1, 1
while length < 1000000:
    i += 1
    new_length = length + len(str(i))
    if length<f and new_length>=f:
        s *= int(str(i)[f-length-1])
        f *= 10
    length = new_length
print s
        
    