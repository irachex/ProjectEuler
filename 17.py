a = sum([3,3,5,4,4,3,5,5,4]) #1 to 9
b = sum([3,6,6,8,8,7,7,9,8,8]) #10 to 19
c = sum([6,6,5,5,5,7,6,6]) #20 to 90
l = (a * 9 + b + c * 10)*10 #1 to 9 used 90 times. 10 to 19 used 10 times 20 to 90 used 100 times
l +=  7*900 #100 to be used 900 times
l += a * 100 #For the hundreds
l += 11 # For 1000
l += 3 * 99 * 9 #The ands are used between 1 and 99 in the 100s so 99 times 9 times
print l
