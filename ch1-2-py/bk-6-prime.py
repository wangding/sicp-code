# 1.2.6 素数检查

# 蛮力法

# 检查 n 是否为素数
def square(x): return x * x
def prime1(n):
  # 找 n 的因子
  def find_divisor(test_divisor):
    def divides(a, b): return b % a == 0
    if square(test_divisor) > n: return n
    if divides(test_divisor, n): return test_divisor
    return find_divisor(test_divisor + 1)
  return n == find_divisor(2)

# test
print(prime1(7))
print(prime1(8))

# 费马检查
def expmod(base, exp, m):
  if exp == 0: return 1
  elif exp % 2 == 0: return (square(expmod(base, exp // 2, m)) % m)
  else: return (base * expmod(base, exp - 1, m)) % m

from random import randint
def fermat_test(n):
  def try_it(a): return expmod(a, n, n) == a
  return try_it(randint(1, n - 1))

def prime2(n, times):
  if times == 0: return True
  if fermat_test(n): return prime2(n, times - 1)
  return False

# test
print(prime2(7, 1))
print(prime2(8, 1))
print(prime2(7, 3))
print(prime2(8, 3))