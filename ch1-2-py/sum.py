# 求 1+2+...+n
def sum1(n): # 线性递归
  if n == 0: return 0
  else: return n + sum1(n - 1)

def sum2(n): # 线性迭代
  def sum_iter(total, counter):
    if counter > n: return total
    return sum_iter(total + counter, counter + 1)
  return sum_iter(0, 1)

def sum3(n): # 公式法，等差数列求和公式
  return n * (n + 1) // 2

def sum4(n): # 循环迭代
  total = 0
  for i in range(1, n + 1): total += i
  return total

# test
print(sum1(100))  # 5050
print(sum2(100))  # 5050
print(sum3(100))  # 5050
print(sum4(100))  # 5050