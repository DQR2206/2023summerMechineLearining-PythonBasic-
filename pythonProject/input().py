#输入函数 input() 输入值的类型为str 使用赋值=对输入值进行存储 input函数内引号中内容为提示语 根据提示语进行输入
present = input('大圣想要什么礼物呢')
print(present, type(present))
a = input('a')#输入的均为字符串类型 需要转换 int() +代表字符串连接
b = input('b')
print(int(a) + int(b))
#算数运算符
#+ - * / //（整除）%取余 **幂运算 整除即为将除法结果向下取整
print(9//4)
print(9//-4)
#其中取余公式中 当为一正一负时用公式 余数=被除数-除数*商 9%-4
print(9%-4)
#赋值运算符 从右到左 a=3+4
#支持链式赋值 a=b=c=20 三个变量名指向同一位置即各个变量的id相同 (id value type) 事实上只要值相等id就相等 不同的变量名指向同一个盒子
#支持参数赋值 += -= *= /=
#支持系列解包赋值 a,b,c=1,2,3

#解包赋值的优点 交换两个变量的值
a,b=1,2
a,b=b,a #交换值语句
print(a,b)

#比较运算符  > < >= <= != == 对象的值的比较 结果为bool类型  is  is not对象的id的比较
a=1
b=1
print(a is b)
list1=[1,2,3,4]
list2=[1,2,3,4]
print(list1==list2)
print(list1 is not list2)#相同元素的列表地址不相同
#bool运算符 对bool值进行运算 and  or  not  in  not in 结果同样为bool类型
c,d=1,2
print(c==1 and d==2)
print(c==1 or d<2)
f1=True
f2=False
print(not f1)#取反
#in表示在什么里
s='helloworld'
print('w' in s, 'm' not in s)
#位运算符  将数据转为二进制之后才进行计算 按位与&(对应数位都为1结果才为1)  按位或|(对应数位全为0结果才为0)  左移<<(溢出高位舍弃低位补0)  右移>>（溢出低位舍弃高位补0）
#左移1位*2 右移1位/2
print (1<<2)

#运算符优先级 整体上算术运算符>位运算符>比较运算符>bool运算符>赋值=
#算术运算符中先算乘除后算加减 有幂运算先算幂运算
#位运算中先移位再与再或
