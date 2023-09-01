#else语句的三种搭配方式
# if else      while else     for else
#这一节主要讲循环的else问题
#else 是与循环头进行搭配的 只有循环正常进行到边界退出 才会进入else循环 由break触发的跳出循环不会进入到else语句
for item in range(3):
    s=input('请输入密码\n')
    if s=='123':
        print('yes')
        break
    else :
        print('输入错误 请重新输入')
else :
    print('三次输入机会已经用完')