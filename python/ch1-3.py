# 第 1 章 使用函数构建抽象
# 1.3 定义新的函数

from operator import add, mul
def square(x): return mul(x, x)

# test
square(21) # 441
square(add(2, 5)) # 49
square(square(3)) # 81

def sum_squares(x, y): return add(square(x), square(y))
sum_squares(3, 4) # 25

def g(): return 1
g() # 1
g = 2
g # 2
def g(h, i): return h + i
g(1, 2) # 3

# 1.3.1 环境
# 1.3.2 调用用户定义的函数
# 1.3.3 示例：调用用户定义的函数
# 1.3.4 局部名称
# 1.3.5 选择名称
# 1.3.6 抽象函数

# 1.3.7 运算符

from operator import truediv, floordiv
truediv(5, 4) # 1.25
floordiv(5, 4) # 1