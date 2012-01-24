import os

value_table = "0023456789TJQKA"
def valueof(c):
    return value_table.index(c[0])

def rankof(p):
    # high card
    r = p[0][0]
    v = r
    
    # pair
    pairs = {}
    suits = {}
    for c in p:
        pairs[c[0]] = pairs.get(c[0], 0) + 1
        suits[c[1]] = suits.get(c[1], 0) + 1
    pairs = {k: v for k,v in pairs.iteritems() if v>1}
    
    isConsecutive = True
    for i in range(1, len(p)):
        if p[i][0] != p[i-1][0]-1:
            isConsecutive = False
    
    if len(pairs)>=1:
        r = 15 # one pair
        v = max([k for k,v in pairs.iteritems() if v==2]+[0])
    if len(pairs)>=2:
        r = 16 # two pair
        v = max([k for k,v in pairs.iteritems() if v==2]+[0])
    if pairs and max(pairs.values())==3:
        r = 17 # three of kind
        v = max([k for k,v in pairs.iteritems() if v==3]+[0])
    if isConsecutive is True:
        r = 18 # straight
    if len(suits)==1:
        r = 19 # flush
    if pairs and max(pairs.values())==3 and len(pairs)>1:
        r = 20 # full house
        v = max([k for k,v in pairs.iteritems() if v==3]+[0])
    if pairs and max(pairs.values())==4:
        r = 21 # four of a kind
        v = max(pairs.keys())
    if isConsecutive is True and len(suits)==1:
        r = 22 # straight flush
    if len(suits)==1 and p[0][0]==14 and p[1][0]==13 and p[2][0]==12 and p[3][0]==11 and p[4][0]==10:
        r = 23 # royal flush
    return r, v
    
    
f = open("poker.txt")
#f = ["5H 5C 6S 7S KD 2C 3S 8S 8D TD", # p2 win
#     "5D 8C 9S JS AC 2C 5C 7D 8S QH", # p1 win
#     "2D 9C AS AH AC 3D 6D 7D TD QD", # p2 win
#     "4D 6S 9H QH QC 3D 6D 7H QD QS", # p1 win
#     "2H 2D 4C 4D 4S 3C 3D 3S 9S 9D"] # p1 win
#f = ["5C AD 5D AC 9C 7C 5H 8D TD KS"]
ans = 0
for line in f:
    cards = line.split(" ")
    p1 = [(valueof(c), c[1]) for c in cards[:5]]
    p2 = [(valueof(c), c[1]) for c in cards[5:]]
    p1.sort(lambda x,y: -cmp(x[0], y[0]))
    p2.sort(lambda x,y: -cmp(x[0], y[0]))
        
    r1, v1 = rankof(p1)
    r2, v2 = rankof(p2)
    
    if r1>r2 or r1==r2 and v1>v2 or r1==r2 and v1==v2 and [c[0] for c in p1]>[c[0] for c in p2]:
    #    print "p1"
        ans += 1
    else:
    #    print "p2"
        pass

print ans
    
    
    