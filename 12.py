f = {}

def num_of_divisor(d):
    s = 1
    for k, v in d.iteritems():
        s *= (v+1)
    return s
    
def main():
    prime_list = []
    n = 2
    while True:
        f.update({n:{}})
        for p in prime_list:
            if n%p == 0:
                f[n] = dict(f[n/p])
                if p not in f[n]:
                    f[n].update({p:1})
                else:
                    f[n][p] += 1
                break
        if not f[n]:
            prime_list.append(n)
            f[n] = {n:1}
        
        if n>2:
            d = dict(f[n])
            d.update(f[n-1])
            d[2] -= 1
            total = num_of_divisor(d)
            print n-1, (n-1)*n/2, total
            if total>500:
                print n-1, (n-1)*n/2, total
                return
        n += 1

if __name__ == "__main__":
    main()
    print f[15]
    
            