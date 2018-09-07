#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 3.x 学习笔记
# 其中一些函数与JavaScript进行了对比
# pyhon 与 JavaScript 都是 动态语言, 所以变量类型可以相互转换
# python 部分内置属性是大写开头的, 应当注意, 如 False, True, None
# Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648-2147483647
# python 中 没有;
# 不要对小数做 ^ 运算, 会报错

# 廖雪峰的官方网站: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000
# 菜鸟教程: http://www.runoob.com/python/python-tutorial.html

# 打印文本, 相当于 console.log
print('hello world')
print('hello', 'world')

# 定义变量, 相当于 var, python没有常量
name = 'mtshen'
PI = 3.1415926
print('name:', name, '\r\n', 'PI:', PI)

# && 运算
f1 = True and True
print('f1:', f1)

# || 运算
f2 = True or False
print('f2:', f2)

# ! 运算
f3 = not False
print('f3:', f3)

# 求余
f4 = 10 % 3
print('f4:', f4)

# 地板求值, 值始终是整数
f5 = 10 // 3
print('f5:', f5)

# 定义长文本
f6 = '''hello world
hello world
hello world'''
print('f6:', f6)

# 文本转义\
f7 = 'I\'m mtshen!'
print('f7:', f7)

# 定义非转义文本(内容全部不转义)
f8 = r"I'm mtshen"
print('f8:', f8)

# 等待用户输入
# 注意, 这是阻断性的, 用户没有输入完成后面的程序不会继续执行
f9 = input()
print('f9:', f9)

# 格式化字符串 % 运算符
# %s表示用字符串替换
# %d表示用整数替换
# %f表示用浮点数替换
# %x表示用十六进制整数替换
# 如果只有一个%?，括号可以省略
f10 = 'hello, %s' % 'world'
f11 = 'hello %s, %d, %f, %x' % ('world', 100, 100, 100)
print('f10:', f10, '\r\n', 'f11', f11)

# 字符串编码 类似于 String.charCodeAt
f12 = ord('A')
print('f12:', f12)

# 字符串解码 类似于 String.fromCharCode
f13 = chr(97)
print('f13:', f13)

# 定义bytes字符串
f14 = b'\xe4\xbd\xa0\xe5\xa5\xbd \xe4\xb8\x96\xe7\x95\x8c'
print('f14:', f14)

# 编码成为bytes字符串
f15 = '你好 世界'.encode('utf-8')
print('f15:', f15)

# 解码bytes字符串
f16 = b'\xe4\xbd\xa0\xe5\xa5\xbd \xe4\xb8\x96\xe7\x95\x8c'.decode('utf-8')
print('f16:', f16)

# 解码bytes 兼容处理
f17 = b'\xe4\xbd\xa0\xe5\xa5\xbd\xe4'.decode('utf-8', errors='ignore')
print('f17:', f17)

# 计算字符长度
f18 = len('hello world')
f19 = len(b'\xe4\xbd\xa0\xe5\xa5\xbd \xe4\xb8\x96\xe7\x95\x8c')
print('f18:', f18, '\r\n', 'f19:', f19)

# ========================================
# 列表 List 相当于 Array
l1 = ['hello', 'world']
print('l1:', l1)

# 列表长度
l2 = len(['hello', 'world'])
print('l2:', l2)

# 列表倒获取-1就是倒数第一位, 依次类推
l3 = [0, 1, 2, 3, 4, 5][-1]
print('l3:', l3)

# 末尾追加, 相当于push
l4 = [0, 1, 2, 3, 4]
l4.append(5)
print('l4:', l4)

# 插入任意位置
l5 = [0, 1, 2, 3, 4]
l5.insert(2, '5')
print('l5:', l5)

# 删除尾元素 pop, 如果传入值则删除指定的位置
l6 = [0, 1, 2, 3, 4, 5]
l6.pop(1)
print('l6:', l6)

# 元组 Tuple 相当于 new Array(X), 他的长度是不可变化的
t1 = ('hello', 'world')
print('t1:', t1)

# 打印某一位, 与list一致
t2 = ('hello', 'world')[0]
print('t2:', t2)

# 判断
a1 = 100
if a1 > 50:
  print('a1: a1 > 50')

# else
a2 = 40
if a1 > 50:
  print('a2: a2 > 50')
else:
  print('a2: a2 < 50')

# elif
a3 = 50
if a3 > 50:
  print('a3: a3 > 50')
elif a3 == 50:
  print('a3: a3 = 50')
else:
  print('a3: a3 < 50')

# 转换字符串为整数 int
a4 = int('100')
print(a4)


# 练习
# 请根据BMI公式（体重除以身高的平方）计算BMI指数，并根据BMI指数：
# 体质指数（BMI）= 体重(kg) ÷ 身高^2(m)
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

print('练习1: BMI')
weight = float(input('weight(kg): '))
height = float(input('height(m): '))
bim = weight / (height * height)

print('你的BIM指数为: %s' % bim)
if bim < 18.5:
  print('你的体重过轻了')
elif bim < 25:
  print('你的体重正常')
elif bim < 28:
  print('你的体重过重了')
elif bim < 32:
  print('你的体重过于肥胖')
else:
  print('你的体重严重肥胖')

# ======================================
# 循环 

# for...in...
x1 = [1, 2, 3, 4, 5]
for x in x1:
  print('x1 循环:', x)

# while
x2 = 0
while x2 > 10:
  x2 = x2 + 1
  print('x2 循环:', x2)

# 生成整数序列
x3 = range(5)
print('x3:', x3)

# 转换成list
x4 = list(range(5))
print('x4:', x4)

# break结束循环
x5 = list(range(100))
for x in x5:
  if x == 10:
    break
  else:
    print('x5 循环:', x)

# 跳出某一次循环 continue
x6 = list(range(10))
for x in x6:
  if x == 6:
    continue
  else:
    print('x6 循环:', x)

# Dict字典,类似Object
# key 必须加引号, 不能使用.运算符, 如果没有符合的key会报错

d1 = { 'name': 'mtshen' }
print('d1:', d1)
print('d1 name:', d1['name'])

# 判断key是否存在
d2 = 'name' in { 'name': 'mtshen' }
print('d2:', d2)

# 使用get获取对用value, 如果不存在不会报错会返回None或自己预定的字符
d3 = {'name': 'mtshen'}.get('data')
d4 = {'name': 'mtshen'}.get('data', 'hello world')
print('d3:', d3, '\r\n', 'd4:', d4)

# 删除某个key
d5 = {'name': 'mtshen', 'data': 'hello world'}
d5.pop('data')
print('d5:', d5)

# Set 键不可重复
s1 = set([1, 1, 2, 2, 3, 3]) # {1, 2, 3}
print('s1:', s1)

# 添加键
s2 = set([1, 2, 3])
s2.add(4) # {1, 2, 3, 4}
print('s2:', s2)

# 删除键
s3 = set([1, 2, 3, 4, 5])
s3.remove(4) # {1, 2, 3, 5}
print('s3:', s3)

# =====================================================
# 函数
# 一些常用函数与JavaScript函数差不多, 如
# abs(): Math.abs(), max(): Math.max(), min(): Math.min()
# int(): Number.parseInt(), float(): Number.parseFloat(), bool(): Boolean()

# 定义函数 def
def fn1(x):
  print('fn1:', x)

fn1('hello world')

# 定义空函数
def fn2():
  pass

fn2()

# 类型检查 isinstance
type1 = isinstance(1, int)
print('type1', type1)

# 多类型检查
type2 = isinstance(1, (int, float))
print('type2', type2)

# 主动抛出类型错误
# 几种错误类型
# TypeError 类型错误
# SyntaxError 语法错误
# IndexError 索引错误
# AttributeError 属性错误
# KeyError 关键字错误
# ValueError 可能为字符串字串错误
# IndentationError 缩进错误
# 更多详见 https://blog.csdn.net/Karen_Yu_/article/details/78629918
# raise TypeError('type error!') # 报错会阻断程序运行, 解注释可执行

# 返回值 return
def fn3():
  return 'hello world'

print('fn3:', fn3())

# 多返回值
def fn4():
  return 100, 500 # 相当于返回了一个tuple元素(100, 500), 返回值可省略括号

fnr1, fnr2 = fn4() # 接收返回值
print('fn4:', fnr1, fnr2)

# 预设默认值, 设置预设值后执行函数, 可以不传入指定参数
# !! python 中不要对预设的List, Dict, Set等可变类型值直接进行修改
# 因为默认参数共同指向了同一个不变对象 ！！！
def fn5(name = 'mtshen'):
  print('fn5:', name)

fn5()

# 不限定长度函数, 参数加*
# * 相当于 函数中的参数解构
def fn6(*angs):
  print('f6:', angs)

fn6(1, 2, 3, 4, 5)

# 部分参数解构, 如果只有部分参数进行解构, 意味着必须传入参数名, 以 key = value 的形式传入
def fn8(name, value, **data):
  print('fn8:', name, value, data)

fn8('mtshen', 21, a = 5, b = 6, c = 7)

# 利用 * 对传入参数解构
def fn7(name, value):
  print('f7:', name, value)

fn7(*['mtshen', 'hello world'])

# 关键字命名, 限定传入的参数名, 必须以 key = value 的形式传入, 这种方式传入, 不限定传入顺序
# * 后的参数必须以 key = value 的形式传入
def fn9(*, name, age):
  print('fn9:', name, age)

fn9(age = 21, name = 'mtshen')

# 如果参数中存在 *key 那么等同于 *, 后面的参数必须以 key = value 的形式传入
def fn10(name, *agrs, age):
  print('fn10:', name, agrs, age)

fn10('mtshen', 1, 2, 3, 4, 5, age = 21)

# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数
# 这5种参数都可以组合使用
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 如
def fn11(name, age = 21, *agrs, **kw):
  pass

# ===================================================
# python 特性

# 切片, list切片即获取某一区间的数组内容
# 可以使用[min:max], [:max], [min:] 也可以输入负值, 表述倒数位置
# 切片同样适用于字符串, list, 元组, 字典, set
qp1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10][1:4] # 1 - 4 但不包含 4, 
print('qp1:', qp1)

# 利用切片浅拷贝
qp2 = qp1[:]
print('qp2:', qp2)

# 利用切片间隔取值
qp3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10][::2] # 每间隔 2 个便取值
print('qp3:', qp3)

# 切片间隔取值2
qp4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10][:5:2] #下标为5 之前每间隔 2 个取值
print('qp4:', qp4)

# 迭代
# 迭代中使用下标 enumerate 可以将 ['name'] 转换成 [(0, 'name')]
dd1 = ['name', 'age', 'data', 'value']
for index, data in enumerate(dd1):
  print('dd1:', index, data)

# 列表生成器
# 如果要生成 1, 2, 3, 4, 5 可以使用
list1 = [x for x in range(1, 6)]
print('list1:', list1)

# 列表生成器基本结构是
# [结果表达式 for...in...{1,} if{0,}]
# 如
list2 = ['value:' + str(value) for value in range(1, 11) if value > 5 ]
print('list2:', list2)

# 列表生成器中 for in 和 if 可以写多个, 进行迭代
# 有木有很唬人, 其实原理很简单
list3 = [(x, y) for x in range(1, 10) for y in range(1, 10) if x > 5 if y > 5]
print('list3:', list3)

# 生成器
# 生成器的目的在于计算一组有规律的列表内容, 在大量内容的情况下, 能够减少内存的占用
# 写法与列表生成器一致, 只不过 [] 变成 ()
sc1 = (x * 6 for x in range(999999999)) # 生成 999999999 个数据
print('sc1:', sc1)

# 生成器可以用for in 遍历外, 还可以使用next来取得下一个生成内容
sc2 = next(sc1)
print('sc2:', sc2)

# yield 关键字创建生成器
#当使用 yield 时, 你的函数将变成生成器 generator, 每次next, 会执行到下一个 yield
def yieldfn():
  yield 1
  yield 3
  yield 5
  yield 7

yieldfn0 = yieldfn()
yieldfn1 = next(yieldfn0)
yieldfn2 = next(yieldfn0)
yieldfn3 = next(yieldfn0)
yieldfn4 = next(yieldfn0)
print('yieldfn:', yieldfn)
print('yieldfn next:', yieldfn1)
print('yieldfn next:', yieldfn2)
print('yieldfn next:', yieldfn3)
print('yieldfn next:', yieldfn4)

# 迭代器
# 判断属性是否可以迭代, 前提是要引入 Iterable
# from collections import Iterable
# isinstance([], Iterable)

# 字符转迭代
# isinstance(iter('hello world'), Iterable)