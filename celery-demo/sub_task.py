#!/usr/bin/env python
from celery_app import app
import time

@app.task
def sub(x, y):
  print(f"计算减法：({x}, {y})")
  time.sleep(5)
  return x - y