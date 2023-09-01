#单分支结构 if ... ...
#双分支结构 if ... else ...
#多分支结构 if  elif elif else
money=1000
s=int(input('请输入取款金额\n'))#input函数输入字符串 int()函数进行转换
if money >= s:
    money = money-s
    print('取款成功 余额为:', money)
else:
    print('余额不足 赶紧滚')

num=int(input('请输入一个整数'))
if num%2==1:
    print(num,'是奇数')
else:
    print(num,'是偶数')

num=int(input('请输入你的成绩\n'))
if num>=90 and num<=100:#或 90<=num<=100
    print('你的成绩为A')
elif num>=80 and num<90:
    print('你的成绩为B')
elif num>=70 and num<80:
    print('你的成绩为C')
elif num>=60 and num<70:
    print('你的成绩为D')
elif num>=0 and num<60:
    print('你不及格')
else:
    print('输入成绩无效')
#嵌套if
s=input('你有会员卡吗\n')
money=int(input('本次消费金额为\n'))
if s=='yes':
    if money>=200:
        money=money*0.8
    elif 100<=money:
        money=money*0.9
    else :
        money=money*1.0
else:
    if money>=200:
        money=money*0.9
    else:
        money=money*1.0
print('打折后的金额为', money)
a=input('请输入a\n')
b=input('请输入b\n')
print('a>=b' if int(a) >= int(b) else 'a<b')#条件表达式