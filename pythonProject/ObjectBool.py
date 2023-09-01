#对象的bool值 以下对象的bool值为false
'''
False 0 空字典 空字符串 None 空列表 空元组等等
'''
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))#空列表
print(bool(list()))#空列表
print(bool(()))#空元组
print(bool(tuple()))#空元组
print(bool({}))#空字典
print(bool(dict()))#空字典
print(bool(set()))#空集合
#即 表示“空”“0”概念的情况bool值为False 其他都为True