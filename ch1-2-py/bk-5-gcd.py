# 1.2.5 求最大公约数 GCD, Greatest Common Divisor
def gcd(a, b): return a if b == 0 else gcd(b, a % b)

# test
print(gcd(206, 40))