# 第 2 章 使用数据构建抽象
# 2.4 可变数据

# 面向对象编程的核心就是向数据添加状态

# 2.4.1 对象隐喻

# 对象将数据的值和行为结合到了一起。
# 对象可以直接表示某些信息，
# 也可以用自身的表现行为来表达想表达的东西。

# date 类型的对象
from datetime import date
tues = date(2014, 5, 13)
print(date(2014, 5, 19) - tues) # 6 days, 0:00:00
tues.year
tues.strftime('%A, %B %d')

# 内置类型的对象
'1234'.isnumeric() # True
'rOBERT dE nIRO'.swapcase() # 'Robert De Niro'
'eyes'.upper().endswith('YES') # True

# 2.4.2 序列对象

# 基本数据类型的实例是不可变（immutable）
# 列表就是可变的（mutable）

chinese = ['coin', 'string', 'myriad']  # 一组字符串列表
suits = chinese                         # 为同一个列表指定了两个不同的变量名

suits.pop()             # 从列表中移除并返回最后一个元素
suits.remove('string')  # 从列表中移除第一个与参数相同的元素

suits.append('cup')              # 在列表最后插入一个元素
suits.extend(['sword', 'club'])  # 将另外一个列表中的所有元素添加到当前列表最后
suits[2] = 'spade'  # 替换某个元素
suits[0:2] = ['heart', 'diamond']  # 替换一组数据

# 2.4.3 字典
# 2.4.4 局部状态

def make_withdraw(balance):
  """返回一个每次调用都会减少 balance 的 withdraw 函数"""
  def withdraw(amount):
    nonlocal balance               # 声明 balance 是非局部的
    if amount > balance: return '余额不足'
    balance = balance - amount       # 重新绑定
    return balance
  return withdraw

withdraw = make_withdraw(100)
# withdraw(25)

# 2.4.5 非局部赋值的好处
# 2.4.6 非局部赋值的代价
# 2.4.7 列表和字典实现
# 2.4.8 调度字典

# 2.4.9 约束传递

# 这个是学习的重点