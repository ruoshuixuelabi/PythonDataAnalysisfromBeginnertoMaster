import numpy as np
n= np.array([0, 30, 45, 60, 90])
print('不同角度的正弦值：')
# 通过乘 pi/180 转化为弧度
print(np.sin(n * np.pi / 180))
print('数组中角度的余弦值：')
print(np.cos(n * np.pi / 180))
print('数组中角度的正切值：')
print(np.tan(n * np.pi / 180))