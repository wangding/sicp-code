# 练习 1.1
10
5 + 3 + 4
9 - 1
6 / 2
((2 * 4) + (4 - 6))
a = 3
b = a + 1
(a + b + (a * b))
a == b
if (b > a) and (b < (a * b)): print(b)
else: print(a)

if a == 4:   print(6)
elif b == 4: print(6 + 7 + a)
else:        print(25)

print(2 + (b if b > a else a))

if a > b:   x = a
elif a < b: x = b
else:       x = -1
print(x * (a + 1))