#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pyHook
import pythoncom
import maps.war3  # 载入WAR3快捷键映射

# 加载所有模块
PATTERN_LISTS = {
  'war3': maps.war3.KEYBOARD_MAP,
}

# 当前使用的模块
GLOBAL_PATTERN_LIST = []

# 键盘钩子是否启动中
GLOBAL_KEYBOARD_STATUS = False

# 按键钩子捕获
def onKeyboardEvent(event):
  global GLOBAL_KEYBOARD_STATUS

  # 获取当前按键
  CURRENT_KEY = event.Key.upper()

  # 默认按键 F4 暂时关闭/开启 键盘
  if CURRENT_KEY == 'F4':
    if GLOBAL_KEYBOARD_STATUS:
      endHook()   # 关闭键盘映射
    else:
      startHook() # 开启键盘映射
  elif GLOBAL_KEYBOARD_STATUS:
    # 模块设置按键
    for (key, keyCallback) in GLOBAL_PATTERN_LIST:
      if key == CURRENT_KEY:
        keyCallback()
        print('[%s] Keyboard mapping Success!' % key)
        break

  return True

# 开启键盘映射
def startHook():
  global GLOBAL_KEYBOARD_STATUS
  GLOBAL_KEYBOARD_STATUS = True

# 关闭键盘映射
def endHook():
  global GLOBAL_KEYBOARD_STATUS
  GLOBAL_KEYBOARD_STATUS = False

# 创建键盘钩子
def initHook():
  hook = pyHook.HookManager()
  hook.KeyDown = onKeyboardEvent
  hook.HookKeyboard()
  pythoncom.PumpMessages()

# 初始化按键钩子
def init(patternType):
  global GLOBAL_PATTERN_LIST
  GLOBAL_PATTERN_LIST = list(PATTERN_LISTS[patternType])

  # 创建键盘钩子
  initHook()

  # 开启键盘映射
  startHook()
