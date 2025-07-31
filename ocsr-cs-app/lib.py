import os

img_path = {
  'input':  './input-images/',
  'output': './output-images/',
}


ports = {
  'next':    65432,
  'decimer': 65433,
  'scribe':  65434,
}


def extract_filename(filepath):
  '''
  提取文件名
  >>> extract_filename('/p/a/t/h/file.xyz')
  'file'
  >>> extract_filename('./p/a/t/h/file.xyz')
  'file'
  >>> extract_filename('file.xyz')
  'file'
  '''
  basename = os.path.basename(filepath)
  filename_without_ext = os.path.splitext(basename)[0]
  return filename_without_ext


def input_img(data):
  '''
  构造输入图片名，包含相对路径
  >>> input_img(b'demo.png')
  './input-images/demo.png'
  '''
  return img_path['input'] + data.decode().strip()


def output_img(data):
  '''
  构造输出图片名，包含相对路径
  >>> output_img(b'test.png')
  './output-images/test.svg'
  '''
  imgf   = data.decode().strip()
  output = img_path['output'] + extract_filename(imgf) + '.svg'
  return output
