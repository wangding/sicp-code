#!/usr/bin/env python

import sys
from add_task import add
from sub_task import sub

if len(sys.argv) != 4:
  print("Usage: python demo.py <task_name> <x> <y>")
  sys.exit(1)

opt = sys.argv[1]
x = int(sys.argv[2])
y = int(sys.argv[3])

result = eval(opt+'.delay(x, y)')
print(f"Task ID: {result.id}")
print(f"Result: {result.get(timeout=10)}")