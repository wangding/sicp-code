# 第 1 章 使用函数构建抽象
# 1.5 控制

# 1.5.1 语句
# 1.5.2 复合语句

# 1.5.3 定义函数 II：局部赋值
def percent_difference(x, y): return 100 * abs(x - y) / x
print(percent_difference(40, 50))

# 1.5.4 条件语句

# 1.5.5 迭代

# 1.5.6 测试

# assert 断言来测试，断言包括两部分
# 1. 条件表达式
# 2. 错误消息（可选）
assert(max(3, 5) == 5, '3, 5 中的最大值应该是 5')

def fn_test():
  assert(max(3, 5) == 5, '3, 5 中的最大值应该是 5')
  assert(max(1, 2, 3) == 3, '1, 2, 3 中的最大值应该是 3')

fn_test()

# 当在文件中而不是直接在解释器中编写 Python 时，
# 测试通常是在同一个文件或带有后缀 _test.py 的相邻文件中编写的。

# 文档测试，不用写 assert 语句了
def sum_naturals(n):
  """返回前 n 个自然数的和。

  >>> sum_naturals(10)
  55
  >>> sum_naturals(100)
  5050
  """
  total, k = 0, 1
  while k <= n: total, k = total + k, k + 1
  return total

if __name__ == "__main__":
  # 方式一：测试整个模块
  from doctest import testmod
  testmod()

  # 方式二：测试单个函数
  from doctest import run_docstring_examples
  run_docstring_examples(sum_naturals, globals(), True)

  # 方式三：不用上面两种方式的测试代码，直接命令行测试
  # python -m doctest -v .\ch1-5.py