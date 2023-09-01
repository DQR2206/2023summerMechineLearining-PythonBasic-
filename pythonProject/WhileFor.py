#初始化变量 条件判断 条件执行体 改变变量
#while循环
a=0
sum=0
while a<101:
    sum=sum+a
    a=a+2
print(sum)
#for in 循环
#for in 表达的对象必须为可迭代对象 如字符串 序列 字典
#in表达从对象中依次取值，又称为遍历
#   for 自定义变量 in 可迭代对象:
#       循环体 #如果循环体内不需要访问自定义变量，就可以将自定义变量替换为_
for item in 'python':
    print(item)
for i in range(10):
    print(i)
#循环体中不需要自定义变量
for _ in range(10):
    print('1')
sum=0
for i in range(0,101,2):
    sum=sum+i
print(sum)
#break语句 用于结束循环结构 跳出最内层循环
#continue 结束当前循环 进入下一个循环
