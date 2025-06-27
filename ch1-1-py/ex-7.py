# 练习 1.7 将牛顿法的绝对误差检查改成相对误差检查
def sqrt(x):
  def average(x, y): return (x + y) / 2
  def good_enough(guess):
    next_guess = improve(guess)
    return abs(next_guess - guess) < (guess * 0.001)
  def improve(guess): return average(guess, x / guess)
  def sqrt_iter(guess):
    if good_enough(guess): return guess
    return sqrt_iter(improve(guess))
  return sqrt_iter(1.0)

# test
print(sqrt(9))  # 3.00009155413138
print(sqrt(100 + 37))  # 11.704699917758145
print(sqrt(sqrt(2) + sqrt(3)))  # 1.7739279023207892
print(sqrt(0.25))  # 0.5

# 很小的数和很大的数表现都非常好
print(sqrt(0.0001))  # 0.010000714038711746
print(sqrt(10000886699))  # 100010.02267281363