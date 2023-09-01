#1.输出函数 print
#可以输出数字  print (77)
#输出字符串 print('helloworld')  print("helloworld")
#含有运算符的表达式 print(1+2)
print(12)
print('dqr in buaa')
print(1+2)
#输出内容的目的地 显示器 文件
#将数据输出到文件  注意点：1.磁盘+文件名 2.print中 file=指针
fp = open('D:/text.txt', 'a+')#a+如果文件存在就在文件后面追加 不存在就创建文件
print('helloworld', file=fp)
fp.close()
#print默认换行输出 不进行换行输出 逗号隔开
print('hello', 'dqr')
#取消print自动换行符的方法是 end 函数
print('杜启嵘是你父亲',end='')

