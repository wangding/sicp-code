#!/usr/bin/env python

import sys
import socket
from lib import ports

def main():
  """
  客户端主函数，负责解析命令行参数、连接服务器并获取计算结果
  """
  if len(sys.argv) != 3:
    print("使用方法: python client.py <image_file> <server_name>")
    sys.exit(1)

  try:
    image_file = sys.argv[1]
    server = sys.argv[2]
  except ValueError:
    print("错误: 请输入有效的图像文件路径或服务名称")
    sys.exit(1)
    
  # 创建 TCP socket 连接，并使用上下文管理器自动关闭连接
  # AF_INET:     使用 IPv4 地址族
  # SOCK_STREAM: 使用 TCP 协议
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
      s.connect(('localhost', ports[server]))

      data = image_file
      s.sendall(data.encode())
      print(f"已发送数据: {image_file}")
      
      result = s.recv(16 * 1024)
      result = eval(result)
      
      # 解码并打印结果
      print("服务器返回结果: ")
      print(result['smiles'])
      print(result['molfile'])

    except ConnectionRefusedError:
      print("错误: 无法连接到服务器，请确保服务器已启动")
      sys.exit(1)
    except Exception as e:
      print(f"发生错误: {str(e)}")
      sys.exit(1)

if __name__ == "__main__": main()
