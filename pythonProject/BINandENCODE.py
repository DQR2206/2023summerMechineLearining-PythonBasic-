#二进制与字符编码
#一个字节八位二进制 1byte=8bit  1024byte=1kb 1024kb=1mb 1024mb=1gb...
#一个字节8位 256种状态 ASC码表  A（65）
#ASC GB2312 GBK GB18030 Unicode UTF-8(英文一个字节 中文三个字节)
#python中保留字和标识符
#输出保留字
import keyword
print(keyword.kwlist)
#标识符 数字字母下划线 不能以数字开头
#变量
#变量由三部分组成
#标识：对象存储的内存地址 使用内置函数id来获取
#类型 对象的数据类型 内置函数type
#值   具体数据
name='dqr in buaa'
print('标识',id(name))
print('类型',type(name))
print('值',name)

#数据类型 int float bool(True Flase) str
#整数类型 int 十进制(默认) 二进制0b 八进制0o 十六进制 0x
print(0b101)#5
#浮点数计算  浮点数存储不精确性 利用浮点数计算时可能会出现小数位数不确定的情况
print(1.1+2.2)
#解决方法 导入 decimal
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))
#bool True->1 False->0
print(True+True)
#str ''或""在一行显示 '''  '''可以在多行显示
s='''
buaa 
dqr
computer science
'''
print(s)

#数据类型转换
# 函数 str()转换为字符串类型 也可用引号转换
# int()转换为整数 1.文字类和小数类字符串无法转换为整数 2.浮点数转换为字符串 舍弃小数部分  即整数类字符串和小数
# float()转换为浮点数 文字类无法转换 整数后加.0
name = '杜启嵘'
age = 20
print('我叫'+name+'今年'+str(age)+'岁')# +为连接符 不同数据类型连接报错
a='190.78'
print(float(a))
#注释 单行注释
#多行注释 一对三引号之间的代码 ''' '''
'''
多行注释
'''
#中文编码声明注释，在文件开头加上中文声明注释 用以指定源码文件的编码格式
#coding:gbk
#coding:utf-8