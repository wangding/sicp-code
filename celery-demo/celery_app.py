#!/usr/bin/env python
import celery
import os
import sys

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 共享Celery应用配置
backend = 'redis://127.0.0.1:6379/1'
broker = 'redis://127.0.0.1:6379/2'
app = celery.Celery('celery_tasks', backend=backend, broker=broker)
app.conf.worker_concurrency = 4

# 显式导入任务模块，确保Celery能发现这些任务
import add_task
import sub_task