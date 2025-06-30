# 练习 1.9
def inc(x): return x + 1
def dec(x): return x - 1

def plus_1(a, b):  # 线性递归
  if a == 0: return b
  else: return inc(plus_1(dec(a), b))

def plus_2(a, b):  # 线性迭代
  if a == 0: return b
  else: return plus_2(dec(a), inc(b))

# test
print(plus_1(3, 4))
print(plus_2(3, 4))