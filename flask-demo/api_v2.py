#!/usr/bin/env python

from flask import Flask, request, Blueprint

# 创建 Flask 应用实例
app = Flask(__name__)

# 创建 Blueprint
cal = Blueprint('cal', __name__)

@cal.route('/add', methods=['GET'])
def add():
  x = int(request.args.get('x'))
  y = int(request.args.get('y'))
  result = x + y
  return {'result': result}

@cal.route('/sub', methods=['POST'])
def sub():
  x = int(request.form.get('x'))
  y = int(request.form.get('y'))
  result = x - y
  return {'result': result}

# 将 Blueprint 注册到 app
app.register_blueprint(cal)

# --- 测试用的 curl 示例 ---
"""
curl "http://localhost:5000/add?x=1&y=2"
curl -X POST -d "x=3&y=1" http://localhost:5000/sub
"""

if __name__ == '__main__': app.run(debug=True)
