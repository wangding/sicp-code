# 练习 1.8 求立方根
def cbrt(x):
  def improve(guess): return (x / (guess * guess) + 2 * guess) / 3
  def good_enough(guess):
    next_guess = improve(guess)
    return abs(next_guess - guess) < guess * 0.001
  def cbrt_iter(guess):
    if good_enough(guess): return guess
    else: return cbrt_iter(improve(guess))
  return cbrt_iter(1.0)

# test
print(cbrt(9))           # 2.0801035255095734
print(cbrt(0.25))        # 0.6304661123708742
print(cbrt(0.0001))      # 0.046419202576589325
print(cbrt(10000886699)) # 2154.5043672873685
print(cbrt(8))           # 2.000004911675504