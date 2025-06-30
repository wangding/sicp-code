# 1.2.2 树形递归

# 斐波那契数列
def fib1(n): # 树形递归版本
  if n < 2: return n
  else: return fib1(n-1) + fib1(n-2)

def fib2(n): # 线性迭代版本
  def fib_iter(a, b, count):
    if count == n: return a
    return fib_iter(b, a+b, count+1)
  return fib_iter(0, 1, 0)

# test
print(fib1(6))
print(fib2(6))