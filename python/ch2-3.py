# 第 2 章 使用数据构建抽象
# 2.3 序列

# 2.3.1 列表

digits = [1, 8, 2, 8]
len(digits) # 4
digits[3] # 8
[2, 7] + digits * 2 # [2, 7, 1, 8, 2, 8, 1, 8, 2, 8]

pairs = [[10, 20], [30, 40]]
pairs[1] # [30, 40]
pairs[1][0] # 30

# 2.3.2 序列遍历

def count(s, value):
  """统计在序列 s 中出现了多少次值为 value 的元素"""
  total, index = 0, 0
  while index < len(s):
    if s[index] == value: total = total + 1
    index = index + 1
  return total
count(digits, 8) # 2

# for 循环简化序列的遍历
def count(s, value):
  """统计在序列 s 中出现了多少次值为 value 的元素"""
  total = 0
  for elem in s:
    if elem == value: total = total + 1
  return total
count(digits, 8) # 2

pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
same_count = 0
for x, y in pairs: # 序列解包
  if x == y: same_count = same_count + 1
same_count # 2

# range
range(1, 10)  # 包括 1，但不包括 10
list(range(5, 8))  # [5, 6, 7]

for _ in range(3): print('Go Bears!')

'''
Go Bears!
Go Bears!
Go Bears!
'''

# 2.3.3 序列处理

# 列表导出式
odds = [1, 3, 5, 7, 9]
[x+1 for x in odds] # [2, 4, 6, 8, 10]
[x for x in odds if 25 % x == 0] # [1, 5]

# 聚合
def divisors(n):
  # return [1] + [x for x in range(2, n) if n % x == 0]
  return [x for x in range(1, n) if n % x == 0]

divisors(4) # [1, 2]
divisors(12) # [1, 2, 3, 4, 6]

[n for n in range(1, 1000) if sum(divisors(n)) == n] # 完美数 [1, 6, 28, 496]

# 2.3.4 序列抽象
# 2.3.5 字符串
# 2.3.6 树
# 2.3.7 链表