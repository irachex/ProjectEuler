f = {1:1}

def cal(n):
    if n in f:
        return f[n]
    if n%2 == 0:
        f.update({n:cal(n/2)+1})
    else:
        f.update({n:cal(3*n+1)+1})
    return f[n]
        

def main():
    n = 2
    max_cnt = 1
    max_n = 1
    while n<=1000000:
        if max_cnt < cal(n):
            max_cnt = f[n]
            max_n = n
        #print n, f[n]
        n += 1
    print max_n, max_cnt
    #837799


if __name__ == "__main__":
    main()
        