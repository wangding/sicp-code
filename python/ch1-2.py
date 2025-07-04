# 第 1 章 使用函数构建抽象
# 1.2 编程要素

# 1.2.1 表达式
# 1.2.2 调用表达式

max(7.5, 9.5)  # 9.5

# 函数参数的顺序很重要
pow(100, 2) # 10000
pow(2, 100) # 1267650600228229401496703205376

# 函数参数不限
max(1, -2, 3, -4) # 3

# 函数参数可以是表达式，实现嵌套
max(min(1, -2), min(pow(3, 5), -4)) # -2

# 1.2.3 导入库函数

from math import sqrt
sqrt(256) # 16.0

from operator import add, sub, mul
add(14, 28) # 42
sub(100, mul(7, add(8, 4))) # 16

# 1.2.4 名称与环境

radius = 10
radius # 10
2 * radius # 20

from math import pi
pi * 71 / 223 # 1.0002380197528042

max

f = max
f # <built-in function max>
f(2, 3, 4) # 4

f = 2
f # 2

max = 5
max # 5
max(2, 3, 4) # TypeError: 'int' object is not callable

area, circumference = pi * radius * radius, 2 * pi * radius
area # 314.1592653589793
circumference # 62.83185307179586

radius = 11
area # 314.1592653589793
area = pi * radius * radius
area # 380.132711084365

x, y = 3, 4.5
y, x = x, y
x # 4.5
y # 3

# 1.2.5 求解嵌套表达式

sub(pow(2, add(1, 10)), pow(2, 5)) # 2016
sub(2048, 32) # 2016

# 1.2.6 非纯函数 print

print(print(1), print(2))