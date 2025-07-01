# 第 1 章 使用函数构建抽象
# 1.7 递归函数

def sum_digits(n):
  """
  返回正整数 n 的所有数字位之和
  >>> sum_digits(9)
  9
  >>> sum_digits(18117)
  18
  >>> sum_digits(9437184)
  36
  >>> sum_digits(11408855402054064613470328848384)
  126
  """
  if n < 10: return n
  else:
    all_but_last, last = n // 10, n % 10
    return sum_digits(all_but_last) + last

# 1.7.1 递归函数剖析

def fact_iter(n):
  '''
  迭代计算阶乘
  >>> fact_iter(4)
  24
  '''
  total, k = 1, 1
  while k <= n: total, k = total * k, k + 1
  return total

def fact(n):
  '''
  递归计算阶乘
  >>> fact(5)
  120
  '''
  if n == 0: return 1
  else: return n * fact(n - 1)

# 1.7.2 互递归
# 间接递归

'''
奇偶数的定义：
如果一个数比一个奇数大 1，那它就是偶数
如果一个数比一个偶数大 1，那它就是奇数
0 是偶数
'''

def is_even(n): return True  if n == 0 else is_odd(n-1)
def is_odd(n):  return False if n == 0 else is_even(n-1)

print(is_even(10))  # True
print(is_odd(11))   # True

# 把间接递归改成直接递归
def is_even2(n):
  if n == 0: return True
  if n == 1: return False
  return is_even2(n-2)

print(is_even2(10))  # True
print(is_even2(11))  # False

# 1.7.3 递归函数中的打印
# 通过对 print 函数的调用，递归函数的计算过程通常可以可视化

def cascade(n):
  """打印数字 n 的前缀的级联"""
  if n < 10: print(n)
  else:
    print(n)
    cascade(n//10)
    print(n)

cascade(2013)

def cascade2(n):
  """打印数字 n 的前缀的级联"""
  print(n)
  if n>10:
    cascade(n//10)
    print(n)

cascade(2013)

# 间接递归，石子游戏，有趣的案例

'''
作为另一个互递归的例子，请思考一个两人博弈的情景，
桌子上最初有 n 个石子，玩家轮流从桌面上拿走一个或两个石子，
拿走最后一个石子的玩家获胜。假设 Alice 和 Bob 在玩这个游戏，
两个人都使用一个简单的策略：
- Alice 总是取走一个石子
- 如果桌子上有偶数个石子，Bob 就拿走两个石子，否则就拿走一个石子
给定 n 个初始石子且 Alice 先开始拿，谁会赢得游戏？
'''
def play_alice(n):
  if n == 0: print("Bob wins!")
  else: play_bob(n-1)

def play_bob(n):
  if n == 0: print("Alice wins!")
  elif is_even(n): play_alice(n-2)
  else: play_alice(n-1)

play_alice(20)
play_alice(25)
play_alice(1)
play_bob(20)
play_bob(25)

# 结论：
# 只有 n = 1 时，且 Alice 先手，Alice 才能赢
# 否则：一定是 bob 赢，考虑问题规模最小 n = 1, 2, 3 时的情况
# 因为无论初始 n 为多少
# 最好问题规模一定会规约到 n = 1, 2, 3 的情况

# 1.7.4 树递归

# 斐波那契数列
def fib1(n): # 树形递归版本
  if n < 2: return n
  else: return fib1(n-1) + fib1(n-2)

# test
print(fib1(6))

# 1.7.5 示例：分割数

'''
求正整数 n 的分割数，最大部分为 m，
即 n 可以分割为不大于 m 的正整数的和，
并且按递增顺序排列。
例如，使用 4 作为最大数对 6 进行分割的方式有 9 种
1.  6 = 2 + 4
2.  6 = 1 + 1 + 4
3.  6 = 3 + 3
4.  6 = 1 + 2 + 3
5.  6 = 1 + 1 + 1 + 3
6.  6 = 2 + 2 + 2
7.  6 = 1 + 1 + 2 + 2
8.  6 = 1 + 1 + 1 + 1 + 2
9.  6 = 1 + 1 + 1 + 1 + 1 + 1

使用最大数为 m 的整数分割 n 的方式的数量等于

1) 使用最大数为 m 的整数分割 n-m 的方式的数量，加上
2) 使用最大数为 m-1 的整数分割 n 的方式的数量

要理解为什么上面的方法是正确的，我们可以将 n 的所有分割方式分为两组：
至少包含一个 m 的和不包含 m 的。此外，第一组中的每次分割都是对 n-m 的分割，
然后在最后加上 m。在上面的实例中，前两种拆分包含 4，而其余的不包含。

因此，我们可以递归地将使用最大数为 m 的整数分割 n 的问题转化为两个较简单的问题：
① 使用最大数为 m 的整数分割更小的数字 n-m，
以及 ② 使用最大数为 m-1 的整数分割 n。

为了实现它，我们需要指定以下的基线情况：

- 整数 0 只有一种分割方式
- 负整数 n 无法分割，即 0 种方式
- 任何大于 0 的正整数 n 使用 0 或更小的部分进行分割的方式数量为 0

这个问题的思路跟换零钱很相似，都是两路树形递归
'''

def count_partitions(n, m):
  """
  计算使用最大数 m 的整数分割 n 的方式的数量
  >>> count_partitions(6, 4)
  9
  >>> count_partitions(5, 5)
  7
  >>> count_partitions(10, 10)
  42
  >>> count_partitions(15, 15)
  176
  >>> count_partitions(20, 20)
  627
  """
  if n == 0: return 1
  elif n < 0: return 0
  elif m == 0: return 0
  else: return count_partitions(n-m, m) + count_partitions(n, m-1)