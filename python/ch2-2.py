# 第 2 章 使用数据构建抽象
# 2.2 数据抽象

# 2.2.1 示例：有理数

1/3 # 0.3333333333333333
1/3 == 0.333333333333333300000  # 整数除法得到近似值 True

def add_rationals(x, y):
  nx, dx = numer(x), denom(x)
  ny, dy = numer(y), denom(y)
  return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
  return rational(numer(x) * numer(y), denom(x) * denom(y))

def print_rational(x): print(numer(x), '/', denom(x))

def rationals_are_equal(x, y):
  return numer(x) * denom(y) == numer(y) * denom(x)

# 2.2.2 对

[10, 20]

pair = [10, 20]
pair # [10, 20]

x, y = pair
x # 10
y # 20

pair[0] # 10
pair[1] # 20

from operator import getitem
getitem(pair, 0) # 10
getitem(pair, 1) # 20

# def rational(n, d): return [n, d]
from math import gcd
def rational(n, d):
  g = gcd(n, d)
  return (n//g, d//g)

def numer(x): return x[0]
def denom(x): return x[1]

half = rational(1, 2)
print_rational(half) # 1 / 2
third = rational(1, 3)
print_rational(mul_rationals(half, third)) # 1 / 6
print_rational(add_rationals(third, third)) # 6 / 9

# 2.2.3 抽象屏障

def square_rational(x):
  return mul_rationals(x, x)

# 违反了抽象屏障的情况 1
def square_rational_violating_once(x):
  return rational(numer(x) * numer(x), denom(x) * denom(x))

# 违反了抽象屏障的情况 2
def square_rational_violating_twice(x):
  return [x[0] * x[0], x[1] * x[1]]

# 2.2.4 数据的属性
# ADT

def pair(x, y):
  """Return a function that represents a pair."""
  def get(index):
    if index == 0: return x
    elif index == 1: return y
  return get

def select(p, i):
  """Return the element at index i of pair p."""
  return p(i)

p = pair(20, 14)
select(p, 0) # 20
select(p, 1) # 14