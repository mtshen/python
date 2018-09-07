#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'设置键盘映射时提供的方法'

import win32api
import win32con
import time

# 鼠标左间点击某个位置
def mouseLeftClick(x, y):
  currentX, currentY = win32api.GetCursorPos()
  # 鼠标移动
  win32api.SetCursorPos((x, y))
  time.sleep(.1)
  # 点击事件
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
  time.sleep(.1)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
  time.sleep(.1)
  # 鼠标移动
  win32api.SetCursorPos((currentX, currentY))
  print('mouseLeftClick', x, y)

# 第一个参数可以 传入 top, bottom, left, right, 第二个参数传入浮点数0.01
def getWinPositionCoord(position, percentage):
  WIN_WIDTH = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
  WIN_HEIGHT = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
  if position == 'top':
    return WIN_HEIGHT * percentage
  elif position == 'left':
    return WIN_WIDTH * percentage
  elif position == 'bottom':
    return WIN_HEIGHT * (1 - percentage)
  elif position == 'right':
    return WIN_WIDTH * (1 - percentage)
  else:
    return 0

