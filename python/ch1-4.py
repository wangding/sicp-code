# 第 1 章 使用函数构建抽象
# 1.4 设计函数


# 1.4.1 文档
# 1.4.2 参数默认值

def pressure(v, t, n=6.022e23):
  """计算理想气体的压力，单位为帕斯卡

  使用理想气体定律：http://en.wikipedia.org/wiki/Ideal_gas_law

  v -- 气体体积，单位为立方米
  t -- 绝对温度，单位为开尔文
  n -- 气体粒子
  """
  k = 1.38e-23  # 玻尔兹曼常数
  return n * k * t / v

help(pressure)
pressure(1, 273.15) # 2269.974834
pressure(1, 273.15, 3 * 6.022e23) # 6809.924502