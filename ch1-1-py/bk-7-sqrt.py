# 1.1.7 实例：牛顿法求平方根
def abs(x): return -x if x < 0 else x
def square(x): return x*x
def average(x, y): return (x+y)/2
def improve(guess, x): return average(guess, x/guess)
def good_enough(guess, x): return abs(square(guess)-x)<0.001
def sqrt_iter(guess, x):
  if(good_enough(guess, x)): return guess
  else: return sqrt_iter(improve(guess, x), x)
def sqrt(x): return sqrt_iter(1.0, x)

# test
print(sqrt(9))                  # 3.00009155413138
print(sqrt((100+37)))           # 11.704699917758145
print(sqrt((sqrt(2)+sqrt(3))))  # 1.7739279023207892
print(square(sqrt(1000)))       # 1000.000369924366
print(sqrt(0.25))               # 0.5001524390243902