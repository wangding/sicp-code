# 1.1.6 条件表达式和谓词
def abs1(x):
  if(x > 0):    return x
  elif(x == 0): return 0
  else:         return -x

abs1(1)
abs1(-1)
abs1(0)

# --
def abs2(x):
  if(x < 0): return -x
  else:      return x

abs2(2)
abs2(-2)
abs2(0)

# 三目运算符或条件表达式 value_if_true if condition else value_if_false
def abs3(x): return -x if x < 0 else x

abs3(3)
abs3(-3)
abs3(0)

# and, or, not 逻辑运算
x = 8  # try x=18 
((x>5) and (x<10))

#def ge(x, y): return ((x>y) or (x==y))
def ge(x, y): return (not (x<y))

# test
ge(5, 6)