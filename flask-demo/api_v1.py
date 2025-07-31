#!/usr/bin/env python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
  # 从查询参数中获取 x 和 y
  x = int(request.args.get('x'))
  y = int(request.args.get('y'))
  result = x + y
  return jsonify({'result': result})


@app.route('/sub', methods=['POST'])
def sub():
  # 从请求体表单中获取 x 和 y
  x = int(request.form.get('x'))
  y = int(request.form.get('y'))
  result = x - y
  return jsonify({'result': result})

'''
curl http://localhost:5000/add?x=1&y=2
curl -X POST -d "x=2&y=1" http://localhost:5000/sub
'''

if __name__ == '__main__': app.run(debug=True)
