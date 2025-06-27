# 1.1.8 过程作为黑盒
def sqrt(x):
  def square(x): return x*x
  def average(x, y): return (x+y)/2
  def improve(guess, x): return average(guess, x/guess)
  def good_enough(guess, x): return abs(square(guess)-x)<0.001
  def sqrt_iter(guess, x):
    if(good_enough(guess, x)): return guess
    else: return sqrt_iter(improve(guess, x), x)
  return sqrt_iter(1.0, x)

# test
print(sqrt(9))                  # 3.00009155413138
print(sqrt((100+37)))           # 11.704699917758145
print(sqrt((sqrt(2)+sqrt(3))))  # 1.7739279023207892
print(sqrt(0.25))               # 0.5001524390243902

# 大数和小数的精度问题
print(sqrt(0.0001))             # 0.03230844833048122
print(sqrt(10000886699))        # 100004.43339672497