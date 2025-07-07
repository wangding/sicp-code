# 第 4 章 数据处理
# 4.2 隐式序列

# 一个序列不一定要把每个元素显式存储在计算机的内存中。
# 换句话说，我们可以建立一个对象，它提供对某个序列的访问，
# 而无需事先计算每个元素的值。
# 取而代之，我们只在有需要的时候才计算元素。

r = range(10000,1000000000)
r[45006230] # 45016230

# 当创建 range 实例时，并没有存储此范围内的 999,990,000 整数。
# 反之，range 对像将第一个元素 10,000 添加到索引 45,006,230 来
# 得出元素 45,016,230。按需求来计算值，而不是从现有的表示中去检索他们，
# 这是惰性计算（Lazy computation）的一个范例。
# 在计算机科学中，惰性计算指任何延迟计算，直到需要该值的程序。

# 4.2.1 迭代器

# 对于任何容器，例如 list 或 range，
# 都可以通过调用内置的 iter 函数来获取迭代器。
# 使用内置的 next 函数来访问迭代器的内容。

primes = [2, 3, 5, 7]
type(primes) # <class 'list'>
iterator = iter(primes)
type(iterator) # <class 'list-iterator'>
next(iterator) # 2
next(iterator) # 3
next(iterator) # 53

# 在 Python 中表示没有更多可用值的方式是在调用 next 时
# 引发 StopIteration 异常。可以使用 try 语句来处理此错误。
try:
  next(iterator)
except StopIteration:
  print('No more values')

# 在迭代器上调用 iter 将返回该迭代器，而不是其副本。
w = iter(iterator)  # w 和 iterator 是同一个迭代器

# 4.2.2 可迭代性

# 任何可以产生迭代器的值都称为可迭代值

# 可迭代对象包括：
# 序列值：例如字符串（string）和元组（tuples）
# 容器：例如集合（sets）和字典（dictionaries）
# 迭代器也是可迭代的，因为它们可以传递给 iter 函数。

d = {'one': 1, 'two': 2, 'three': 3}
d # {'one': 1, 'three': 3, 'two': 2}
k = iter(d)
next(k) # 'one'
next(k) # 'three'
v = iter(d.values())
next(v) # 1
next(v) # 3

# 4.2.3 内置迭代器

# map 函数是惰性的：调用它时并不会执行计算，直到返回的迭代器被 next 调用

def double_and_print(x):
  print('***', x, '=>', 2*x, '***')
  return 2*x
s = range(3, 7)
doubled = map(double_and_print, s)  # double_and_print 未被调用
next(doubled)                       # double_and_print 调用一次
# *** 3 => 6 ***
# 6
next(doubled)                       # double_and_print 再次调用
# *** 4 => 8 ***
# 8
list(doubled)                       # double_and_print 再次调用兩次
# *** 5 => 10 ***             # list() 会把剩余的值都计算出来并生成一个列表
# *** 6 => 12 ***
# [10, 12]

# 4.2.4 For 语句



# 4.2.5 生成器和 Yield 语句
# 4.2.6 可迭代接口
# 4.2.7 使用 Yield 创建可迭代对象
# 4.2.8 迭代器接口
# 4.2.9 Streams
# 4.2.10 Python 流
