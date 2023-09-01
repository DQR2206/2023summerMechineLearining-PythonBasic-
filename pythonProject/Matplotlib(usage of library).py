#matplotlib是绘制图表的常规库
import numpy as np
import matplotlib.pyplot as plt
#当只传递一个数组时，将传递的数据视为y,x对应的值为0,1,2,...n
plt.plot([4,3,2,1])
plt.show()
#画图的另一种方式是plt.plot(x,y)
x=np.arange(5)
y=np.arange(100,600,100)
plt.plot(x,y)
plt.show()
x=np.arange(30)
y=[x_i + np.random.rand(1) for x_i in x]#通过循环将每个x加上一个随机的小数
a,b=np.polyfit(x,y,1)#1代表一次拟合，即拟合出一条直线，对x,y进行一次拟合饿到斜率和截距a,b
_=plt.plot(x,y,'o', np.arange(30),a*np.arange(30)+b,'-')#ply.plot()为绘制图像函数 这里分别绘制了两个图象 1.'o'代表圆点 用圆点绘制散点图 2.'-'代表直线 用实线绘制直线
plt.show()#显示绘制的图像
#图表尺寸 plt.figure(figsize=(水平尺寸，垂直尺寸))
plt.figure(figsize=(4,4))
x=np.linspace(0,2*np.pi)#创建均匀间隔的数组 起始位置 结束位置 元素个数 默认元素个数为50
plt.plot(x,np.sin(x))
#为图表添加标题 x轴标签和y轴标签
plt.title('sinx')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
#图表网格
plt.grid()#该函数为绘制网格函数，默认值为ture 可手动在括号内修改为false
#设置图表刻度 利用函数 xticks(显示位置，显示字符)
positions=[0,np.pi/2,np.pi,np.pi*3/2,np.pi*2]
labels=[0,90,180,270,360]
plt.xticks(positions,labels)
#plt.yticks(positions,labels)
plt.show()
#散点图 plt.scatter()
x=np.random.rand(100)
y=np.random.rand(100)
#cmap是颜色贴图 适用预先的绿色颜色图 颜色深浅与y同步变化
#plt.scatter(x,y,s=600,c=y,cmap="Reds")
plt.scatter(x,y,s=600,c="pink",alpha=0.5,linewidths=2,edgecolors="red")#s为点的大小 c是点的颜色 alpha是点的透明度 linwidths是点绘制时的线宽 edgecolors是点边缘的颜色
plt.grid()
plt.show()
#多个图表的网格显示
#subplot(行数 列数 整体的顺序号码)函数 编号为从上往下从左往右
x=np.random.rand(100)
y=np.random.rand(100)
plt.subplot(121)
plt.scatter(x,y,s=300,c="pink",alpha=0.5,linewidths=2,edgecolors="red")
plt.subplot(122)
plt.scatter(x,y,s=300,c=y,cmap="Greens")
plt.show()
#三维散点图
from mpl_toolkits.mplot3d import Axes3D
np.random.seed(0)#随机数生成器的种子为0
random_x=np.random.randn(100)
random_y=np.random.randn(100)
random_z=np.random.randn(100)
fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(1,1,1,projection="3d")
x=np.ravel(random_x)#三组随机数转换为一维数组 np.ravel()是numpy库中的函数 将多维数组转换为一维数组
y=np.ravel(random_y)
z=np.ravel(random_z)
ax.scatter3D(x,y,z,s=300,c='r',marker='^')#maker指形状为三角形
plt.show()
