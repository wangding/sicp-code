# 关于浮点数的精度误差
# 用来说明牛顿法计算 sqrt
# 应该用相对误差，而不是绝对误差

import sys

#返回 x 与下一个可表示的浮点数之间的间隔
def float_spacing(x): return abs(x) * sys.float_info.epsilon

# 测试几个非常大的数
nums = [1.0, 1e6, 1e10, 1e20, 1e100]

print("机器 epsilon:", sys.float_info.epsilon)
print("-" * 40)
for n in nums: print(f"x = {n:9.2e}, 两浮点数的间隔: {float_spacing(n):.2e}")

import math

x = 1e20
next_x = math.nextafter(x, math.inf)
print(f"\n下一个比 {x} 大的浮点数是: {next_x}")
print(f"两者的间隔为: {next_x - x}")