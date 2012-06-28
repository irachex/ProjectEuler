import math

def compare(a, b, c, d):
    return float(b) * math.log(float(a)) > float(d) * math.log(float(c))

def main():
    f = open('base_exp.txt')
    maxa, maxb, maxline = 1, 1, 0
    line_no = 0
    for line in f:
        line_no += 1
        a, b = line.split(',')
        if compare(a, b, maxa, maxb):
            maxa, maxb, maxline = a, b, line_no
    print maxline

if __name__ == "__main__":
    main()




