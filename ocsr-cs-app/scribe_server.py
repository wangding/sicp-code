#!/usr/bin/env python

import types
import torch
import socket
import selectors
from molscribe import MolScribe
from rdkit.Chem import MolFromMolBlock
from rdkit.Chem.Draw import MolToFile
from lib import input_img, output_img, ports

ckpt   = './checkpoints/swin_base_char_aux_1m.pth'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model  = MolScribe(ckpt, device)

sel = selectors.DefaultSelector()

def accept_wrapper(sock):
  """
  处理新的客户端连接请求
  参数sock: 监听套接字
  """
  conn, addr = sock.accept()
  print(f"Accepted connection from {addr}")
  
  conn.setblocking(False)
  
  # 创建一个简单对象存储客户端数据
  # addr: 客户端地址
  # inb:  用于存储接收的数据
  # outb: 用于存储待发送的数据
  data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
  
  events = selectors.EVENT_READ | selectors.EVENT_WRITE
  sel.register(conn, events, data=data)


def service_connection(key, mask):
  """
  处理客户端连接的数据收发和业务逻辑
  参数 key:  包含文件对象和数据的选择器键
  参数 mask: 事件掩码，表示发生的事件类型
  """
  sock = key.fileobj
  data = key.data
  
  if mask & selectors.EVENT_READ:
    recv_data = sock.recv(1024)
    if recv_data:
      output = model.predict_image_file(input_img(recv_data), return_atoms_bonds=False, return_confidence=False)
      data.outb = str(output).encode()
      mol = MolFromMolBlock(output['molfile'])
      MolToFile(mol, output_img(recv_data))
    else:
      print(f"Closing connection to {data.addr}")
      sel.unregister(sock)
      sock.close()
    
  if mask & selectors.EVENT_WRITE:
    if data.outb:
      sent = sock.send(data.outb)
      data.outb = data.outb[sent:]


def main():
  """主函数，启动 scribe 服务器"""
  host, port = "0.0.0.0", ports['scribe']

  # 创建 TCP 套接字
  # AF_INET:     使用 IscribePv4 地址族
  # SOCK_STREAM: 使用 TCP 协议
  lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  lsock.bind((host, port))
  lsock.listen()
  print(f"scribe 服务器正在监听 {(host, port)}")
  
  lsock.setblocking(False)
  sel.register(lsock, selectors.EVENT_READ, data=None)
    
  try:
    while True:
      events = sel.select(timeout=None)
      for key, mask in events:
        if key.data is None: accept_wrapper(key.fileobj)
        else: service_connection(key, mask)
  except KeyboardInterrupt:
    print("接收到键盘中断，正在退出")
  finally:
    sel.close()


if __name__ == "__main__": main()
