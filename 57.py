from fractions import Fraction

ans = 0
n = Fraction(1,2)
for i in range(1000):
    n = n + Fraction(2,1)
    n = Fraction(n.denominator, n.numerator)
    n = n + Fraction(1,1)
    if len(str(n.numerator)) > len(str(n.denominator)):
        ans += 1
    n = n - Fraction(1,1)
print ans
    