# 第 1 章 使用函数构建抽象
# 1.1 开始

# 1.1.1 Python 编程
# 1.1.2 安装 Python 3
# 1.1.3 交互式会话

# 1.1.4 第一个例子

from urllib.request import urlopen
# 这个表达式将 urlopen 函数应用在了一个包含莎士比亚 37 部戏剧完整文本的 URL 上
shakespeare = urlopen('https://www.composingprograms.com/shakespeare.txt')
words = list(shakespeare.read().decode().split())
{w for w in words if len(w) == 6 and w[::-1] in words}
# {'redder', 'drawer', 'reward', 'diaper', 'repaid'}

# 1.1.5 错误