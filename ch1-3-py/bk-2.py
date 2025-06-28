# 1.3.2 用 lambda 构造过程

# lambda x: x + 4
# lambda x: 1.0 / (x * (x + 2))

def sum(term, a, next, b):
  if a > b: return 0
  else: return term(a) + sum(term, next(a), next, b)

# pi-sum 函数不需要定义两个很少用到的函数 pi-term, pi-next
# lambda 匿名函数搞定
def pi_sum(a, b):
  return sum(lambda x: 1.0 / (x * (x + 2)),
             a,
             lambda x: x + 4,
             b)

# test
print(pi_sum(1, 7))  # 0.3619047619047619

# integral 函数不需要定义函数 add-dx, 用 lambda 匿名函数代替
def integral(f, a, b, dx):
  return sum(f,
             a + dx / 2.0,
             lambda x: x + dx,
             b) * dx

# test
def cube(x): return x * x * x
print(integral(cube, 0, 1, 0.01))  # .24998750000000042

def plus4(x): return x + 4
plus4_lambda = lambda x: x + 4
def square(x): return x * x

# 等价于 javascipt 中的函数立即执行表达式
# Immediately Invoked Function Expression, IIFE
print((lambda x, y, z: x + y + square(z))(1, 2, 3))

def f1(x, y):
  def f_helper(a, b): return x * square(a) + y * b + a * b
  return f_helper(1 + x * y, 1 - y)

def f2(x, y):
  return (lambda a, b: x * square(a) + y * b + a * b)(1 + x * y, 1 - y)

def f3(x, y):
  a = 1 + x * y
  b = 1 - y
  return x * square(a) + y * b + a * b