#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'war3 技能释放按键'

import tool

KEYBOARD_MAP = []

def WAR_3_Q():
  x = tool.getWinPositionCoord('right', 0)
  y = tool.getWinPositionCoord('bottom', 0)
  tool.mouseLeftClick(x, y)

def WAR_3_W():
  x = tool.getWinPositionCoord('right', 0)
  y = tool.getWinPositionCoord('bottom', 0)
  tool.mouseLeftClick(x, y)

def WAR_3_E():
  x = tool.getWinPositionCoord('right', 0)
  y = tool.getWinPositionCoord('bottom', 0)
  tool.mouseLeftClick(x, y)

def WAR_3_R():
  x = tool.getWinPositionCoord('right', 0)
  y = tool.getWinPositionCoord('bottom', 0)
  tool.mouseLeftClick(x, y)

def WAR_3_T():
  x = tool.getWinPositionCoord('right', 0)
  y = tool.getWinPositionCoord('bottom', 0)
  tool.mouseLeftClick(x, y)

def WAR_3_D():
  x = tool.getWinPositionCoord('right', 0)
  y = tool.getWinPositionCoord('bottom', 0)
  tool.mouseLeftClick(x, y)

# 绑定键盘映射
KEYBOARD_MAP.append(('Q', WAR_3_Q))
KEYBOARD_MAP.append(('W', WAR_3_W))
KEYBOARD_MAP.append(('E', WAR_3_E))
KEYBOARD_MAP.append(('R', WAR_3_R))
KEYBOARD_MAP.append(('T', WAR_3_T))
KEYBOARD_MAP.append(('D', WAR_3_D))