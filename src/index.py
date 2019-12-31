#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
import maps.main

# 载入配置文件
CONFIG = json.load(open('./config.json', encoding="utf-8"))
CONFIG_TYPE = CONFIG['type']

print('当前配置模式为%s' % CONFIG_TYPE)

# 载入模式
maps.main.init(CONFIG_TYPE)
