#!/bin/bash

start_time=$(date +%s)

# 启动4个客户端（后台并行）
/home/wangding/miniconda3/bin/python ./demo.py add 3 4 &
/home/wangding/miniconda3/bin/python ./demo.py add 5 2 &
/home/wangding/miniconda3/bin/python ./demo.py add 7 8 &
/home/wangding/miniconda3/bin/python ./demo.py add 10 3 &

# 等待所有后台进程完成
wait
echo "所有测试已完成"

end_time=$(date +%s)
echo "运行时间: $((end_time - start_time)) 秒"