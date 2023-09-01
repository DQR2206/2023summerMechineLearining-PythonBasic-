#range函数 用于生成一个整数序列
#用法一 range(stop) 从0开始stop截止 默认步长为1
r=range(10)
print(list(r))#list为列表意
#用法二 range(start,stop) start开始 stop截止 默认步长为1
r=range(1,10)
print(list(r))
#用法三 range(start,stop,step)增加步长参数
r=range(1,10,2)
print(list(r))
#range类型的优点 无论range类型包含多大的整数序列 所占用的内存空间大小是相同的 只需要存储start stop step
#利用 in not in 判断整数序列中是否含有指定元素
print(10 not in r)
print(9 in r)

