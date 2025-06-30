# 1.2.2 树形递归

# 换零钱
def count_change(amount):
  def first_denomination(kinds_of_coins):
    return [1, 5, 10, 25, 50][kinds_of_coins - 1]

  def cc(amount, kinds_of_coins):
    if amount == 0: return 1
    if amount < 0 or kinds_of_coins == 0: return 0
    return cc(amount, kinds_of_coins - 1) + \
           cc(amount - first_denomination(kinds_of_coins), kinds_of_coins)

  return cc(amount, 5)

# test
print(count_change(100))
