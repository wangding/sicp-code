# 第 1 章 使用函数构建抽象
# 1.6 高阶函数

# 1.6.1 作为参数的函数

# 问题 1：a~b 中 n 个连续的数求和，
# 例如：1+2+3+...+100
def sum_integers(a, b):
  return 0 if a > b else a + sum_integers(a + 1, b)

# test
print(sum_integers(1, 100))

# 问题 2：a~b 中 n 个连续的数的立方求和，
# 例如：1^3 + 2^3 +...+ 100^3
def cube(x): return x * x * x
def sum_cubes(a, b):
  return 0 if a > b else cube(a) + sum_cubes(a + 1, b)

# test
print(sum_cubes(1, 3))  # 36

# 问题 3：计算 1/(1*3) + 1/(5*7) + ...
def pi_sum(a, b):
  return 0 if a > b else 1.0 / (a * (a + 2)) + pi_sum(a + 4, b)

# test
print(pi_sum(1, 7))  # 0.3619047619047619

# 从上面三个求和的问题求解中抽取 sum 求和模式，这个是高阶函数
# 其中 term 是根据 a 计算数列中第 i 个数，例如：a^3
# 其中 next 是根据 a 计算下一个 a，例如：a + 1
def summation(term, a, next, b):
  return 0 if a > b else term(a) + summation(term, next(a), next, b)

# 用求和模式求解问题 1
def inc(n): return n + 1
def sum_integers2(a, b):
  def identity(x): return x
  return summation(identity, a, inc, b)

# test
print(sum_integers2(1, 100))

# 用求和模式求解问题 2
def sum_cubes2(a, b): return summation(cube, a, inc, b)

# test
print(sum_cubes2(1, 3))  # 36

# 用求和模式求解问题 3
def pi_sum2(a, b):
  def pi_term(x): return 1.0 / (x * (x + 2))
  def pi_next(x): return x + 4
  return summation(pi_term, a, pi_next, b)

# test
print(pi_sum2(1, 7))  # 0.3619047619047619

# 问题 4，求函数在 [a, b] 区间的定积分的近似值
# 用求和模式求解问题 4
def integral(f, a, b, dx):
  def add_dx(x): return x + dx
  return summation(f, a + dx / 2.0, add_dx, b) * dx

print(integral(cube, 0, 1, 0.01))   # .24998750000000042

# 1.6.2 作为通用方法的函数



# 1.6.3 定义函数 III：嵌套定义

def sqrt(x):
  def square(x): return x*x
  def average(x, y): return (x+y)/2
  def improve(guess, x): return average(guess, x/guess)
  def good_enough(guess, x): return abs(square(guess)-x)<0.001
  def sqrt_iter(guess, x):
    if(good_enough(guess, x)): return guess
    else: return sqrt_iter(improve(guess, x), x)
  return sqrt_iter(1.0, x)

# test
print(sqrt(9))                  # 3.00009155413138
print(sqrt((100+37)))           # 11.704699917758145
print(sqrt((sqrt(2)+sqrt(3))))  # 1.7739279023207892
print(sqrt(0.25))               # 0.5001524390243902

# 大数和小数的精度问题
print(sqrt(0.0001))             # 0.03230844833048122
print(sqrt(10000886699))        # 100004.43339672497


# 1.6.4 作为返回值的函数

def compose1(f, g):
  def h(x): return f(g(x))
  return h

# test
print(compose1(sqrt, sqrt)(16))  # 2

# 1.6.5 示例：牛顿法



# 1.6.6 柯里化

def curried_pow(x):
  def h(y): return pow(x, y)
  return h
curried_pow(2)(3) # 8

def map_to_range(start, end, f):
  while start < end:
    print(f(start))
    start = start + 1

# test
map_to_range(0, 10, curried_pow(2))

# 1.6.7 Lambda 表达式

def compose1(f, g): return lambda x: f(g(x))

# test
print(compose1(lambda x: x + 1, lambda x: x * 2)(3))  # 7

compose2 = lambda f, g: lambda x: f(g(x))

# test
print(compose1(lambda x: x + 1, lambda x: x * 2)(3))  # 7

s = lambda x: x * x
s  # <function <lambda> at 0xf3f490>
s(12) # 144

# 1.6.8 抽象和一等函数
# 1.6.9 函数装饰器

def trace(fn):  # fn 是被装饰的函数
  def wrapped(x):
    print('-> ', fn, '(', x, ')')
    return fn(x)
  return wrapped  # 返回一个新函数

@trace
def triple(x): return 3 * x

print(triple(12))  # ->  triple ( 12 )