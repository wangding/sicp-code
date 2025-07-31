#!/usr/bin/env python
from celery_app import app
import time

@app.task
def add(x, y):
  print(f"计算加法：({x}, {y})")
  time.sleep(5)
  return x + y