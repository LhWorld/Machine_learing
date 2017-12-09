#coding:utf-8
#coding:utf-8
from matplotlib.figure import Figure
from matplotlib.axes import  Axes
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

f = Figure() # 画布对象

# f.set('font.sans-serif'='SimHei')
canvas = FigureCanvas(f)
# ax =Axes()
ax =f.add_axes([0.1,0.1,0.8,0.8]) # axes原点所在整个画布中的比例坐标
line = ax.plot([0,1], [0,1])


# ax.set_title()
ax.set_title("第二张图片",fontproperties='SimHei')
ax.set_xlabel("x value")
ax.set_ylabel("y value")
# f.set_axes()
# f.show()
# canvas.draw()
canvas.print_jpg('dome2.jpg')