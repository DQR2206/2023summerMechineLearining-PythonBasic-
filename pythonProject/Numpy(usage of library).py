#numpy是快速执行数组计算的库
import numpy as np#导入numpy库并命名为np
a=np.array([1,2,3])#numpy的array()函数 用于创建数组
#专门用于创建二维数组的函数 matrix() matrix()函数具有array()的一切功能但只能用于创建二维数组
k=np.matrix([[1,1,1],[2,2,2],[3,3,3]])
#除了手动初始化之外 还可以使用arange()函数生成数组 该函数的用法与range()相同 start stop step 先建立一维数组再转化为二维数组 ndarray.reshape()
dqr=np.arange(10000).reshape((10,1000))
#对数组进行整体运算
#a=a*3
#a+=2
#数组间进行整体运算 即为每一个分量上的对应元素进行计算
b=np.array([1,1,4])
#c=a+b
#c=a/b
#一维向量点积 np中的dot()函数
print(np.dot(a,b))
#二维向量内积 矩阵乘法
c=np.array([[1,2],#这样写好理解一些
            [3,4]])
d=np.array([[3,4],
            [1,2]])
print(np.dot(c,d))#矩阵乘法
#numpy库中对于高维数组的定义是ndarray ndarray中的元素都具有相同类型
#如以上的二维数组，最外围的[]相当于表示里边的元素组成的是一整个数组  里边的[]用,隔开表示每一行 行数和每行中元素的个数影响矩阵的形状
#三维数组中的元素则为用,隔开的二维数组 如  e=np.array([[[3,3,3],[3,3,3]],[[3,3,3],[3,3,3]]])
e=np.array([[[3,3,3],[3,3,3]],[[3,3,3],[3,3,3]]])
#ndarray形状转换
g=np.arange(9).reshape((3,3))#将1*9转换为3*3 行*列
print(g)
#np.ravel()可以将高维数组转换为一维数组
g=np.ravel(g)
print(g)
g=g.reshape((9,1))
print(g)
#生成元素为0的数组 zeros()函数
zeros=np.zeros((3,4))
print(zeros)
#生成元素为1的数组 ones()函数
h=np.ones((3,4))
print(h)
#生成未初始化的数组 empty()函数 其中的数字是随机的，不会被初始化
y=np.empty((3,4))
print(y)
#ndarray.shape()方式获取数组形状
print(y.shape)
#获取元素类型 ndarray.dtype.name
print(y.dtype.name)
#每个元素所占字节数 ndarray.itemsize
print(y.itemsize)
#元素总数  ndarray.size
print(y.size)
#元素类型转换 ndarray.astype('需要转换到的类型')
y=y.astype('int32')
print(y.dtype)