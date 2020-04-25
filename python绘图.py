from matplotlib import pyplot as  plt
import  random
import matplotlib
font = {'family' : 'Microsoft YaHei',
              'weight' : 'bold',
              'size'   : 'larger'}

matplotlib.rc("font")
matplotlib.rc("font",family='Microsoft YaHei')
x = range(0,120)
y = [random.randint(20,35)for i in  range(120)]#在20-35之间选取120个数字
#设置图片大小和分辨率
fig=plt.figure(figsize=(20,8),dpi=80)
#设置x轴刻度
_xtick_labels=["10点{}分".format(i) for  i in range(60)]#在数字后面加上H
_xtick_labels +=["11点{}分".format(i-60) for  i in range(60,120)]
plt.xticks(x[::3],_xtick_labels[::3],rotation=90)#设置标签，保持两者步长相等,rotation=90 标签旋转90度
#添加描述信息
plt.xlabel("时间")
plt.ylabel("10点到10点之间每分钟温度变化")
plt.plot(x,y)
plt.show()
＃添加文字
