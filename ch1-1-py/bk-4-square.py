# 1.1.4 复合过程（就是函数）
# 函数是最重要的抽象
def square(x): return x * x
square

# test
square(21)
square(2+5)
square(square(3))

def sum_of_squares(x, y): return square(x)+square(y)

# test
sum_of_squares(3, 4)

def f(a): return sum_of_squares(a+1, a*2)

# test
f(5)