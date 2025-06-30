# 1.2.1 线性的递归和迭代
# 求阶乘
# 递归版本
def factorial_a(n):
  if(n==1): return 1
  else: return n*factorial_a(n-1)

# test
print(factorial_a(6))

# 迭代递归版本，使用尾递归
def factorial_b(n):
  def fact_iter(product, counter):
    if(counter>n): return product
    else: return fact_iter(counter*product, counter+1)
  return fact_iter(1, 1)

# test
print(factorial_b(6))

# 循环迭代版本
def factorial_c(n):
  result = 1
  for i in range(1, n+1): result *= i
  return result

# test
print(factorial_c(6))