#反斜杠+实现的转义功能首字母
# \n (newline) \r (return) \t (table) \b (back)
#在\t的使用中 \t占四个制表位  下面的输出中 第一个会输出三个空格 第二个会输出四个空格
print('hello\tworld')
print('helloooo\tworld')
#\r \b的使用中都是覆盖式的用法 \r退到已经输出过的行首重新开始写 \b回退一个字符开始写
print('hello\rworld')  #输出world
print('hello\bworld')  #输出hellworld

#字符串中包含 \ ' " 时
print('https:\\infinity-dqr.com')
print('老师说:\'good\'')

#原字符 不希望字符串中的转义字符起作用 在字符串之前加r or R
print(r'hello\nworld')