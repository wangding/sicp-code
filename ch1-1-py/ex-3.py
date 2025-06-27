# 练习 1.3 求三个数中最大两个数的平方和
def max_sum_square(x, y, z):
  def square(x): return x * x
  def sum_square(x, y): return square(x) + square(y)
  if x < y and x < z:   return sum_square(y, z)
  elif y < x and y < z: return sum_square(x, z)
  elif z < x and z < y: return sum_square(x, y)

# test
max_sum_square(3, 4, 5)