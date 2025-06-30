# 1.2.4 求幂 b^n
# 线性递归
def expt1(b, n):
  if n == 0: return 1
  else: return b * expt1(b, n-1)

# 线性迭代
def expt2(b, n):
  def expt_iter(product, counter):
    if counter > n: return product
    return expt_iter(b*product, counter+1)
  return expt_iter(1, 1)

# 快速递归
def expt3(b, n):
  def square(x): return x * x
  if n == 0: return 1
  elif n % 2 == 0: return square(expt3(b, n // 2))
  else: return b * expt3(b, n - 1)

# test
print(expt1(2, 3))
print(expt2(2, 3))
print(expt3(2, 3))