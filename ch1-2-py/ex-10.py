# 练习 1.10
def A(x, y):
  if   y == 0: return 0
  elif y == 1: return 2
  elif x == 0: return 2 * y
  else: return A(x - 1, A(x, y - 1))

# test
print(A(1, 10))  # 1024
print(A(2, 4))   # 65536
print(A(3, 3))   # 65536

def f(n): return A(0, n)
def g(n): return A(1, n)
def h(n): return A(2, n)
def k(n): return 5 * n * n

# test
print(f(3)) # 6
print(g(3)) # 8
print(h(3)) # 16
print(k(3)) # 45