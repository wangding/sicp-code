# 1.3.1 过程作为参数

# 问题 1：a~b 中 n 个连续的数求和，例如：1+2+3+...+100
def sum_integers(a, b):
  return 0 if a > b else a + sum_integers(a + 1, b)

# test
print(sum_integers(1, 100))

# 问题 2：a~b 中 n 个连续的数的立方求和，例如：1^3 + 2^3 +...+ 100^3
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
def identity(x): return x
def inc(n): return n + 1
def sum_integers2(a, b): return summation(identity, a, inc, b)

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