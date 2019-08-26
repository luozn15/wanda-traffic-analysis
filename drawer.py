import math
from matplotlib.lines import Line2D
from matplotlib.patches import Arc
import matplotlib.pyplot as plt

class heatDrawer():
    path = ''

    line = ''
    arc = ''
    ellipse = ''
    lwpline = ''
    xa, xi ,ya, yi =0, 0, 0, 0

    csv = []

    def __init__(self,path):
        self.path = path

    def set_dxf(self,dxfprocessor):
        self.line = dxfprocessor.line
        self.arc = dxfprocessor.arc
        self.ellipse = dxfprocessor.ellipse
        self.lwpline = dxfprocessor.lwpline
        self.xa = dxfprocessor.xa
        self.xi = dxfprocessor.xi
        self.ya = dxfprocessor.ya
        self.yi = dxfprocessor.yi

    def set_csv(self,csv):
        self.csv =csv


    def draw(self):
        xa = self.xa
        xi = self.xi
        ya = self.ya
        yi = self.yi
        line = self.line
        arc = self.arc
        ellipse = self.ellipse
        lwpline = self.lwpline

        figure, ax = plt.subplots(figsize=((xa-xi)/10000,(ya-yi)/10000), dpi=100)

        # 设置x，y值域
        ax.set_xlim(left=xi, right=xa,auto=False)
        ax.set_ylim(bottom=yi, top=ya,auto=False)

        # 底图绘制
        line_xs = [0]*len(line)
        line_ys = [0]*len(line)
        for i in range(len(line)):
            (line_xs[i], line_ys[i]) = zip(*line[i])

        for i in range(len(line_xs)):
            ax.add_line(Line2D(line_xs[i], line_ys[i], linewidth=1, color='blue'))
            
        for i in arc:
            ax.add_patch(Arc(i[0], i[1], i[1], theta1= i[2], theta2=i[3]))
            
        for i in ellipse:
            ax.add_patch(Arc(i[0], i[1], i[2],angle = i[3], theta1= i[4], theta2=i[5]))
            
        lwpl_xs = [0]*len(lwpline)
        lwpl_ys = [0]*len(lwpline)
        for i in range(len(lwpline)):
            (lwpl_xs[i], lwpl_ys[i]) = zip(*lwpline[i])
        for i in range(len(lwpl_xs)):
            ax.add_line(Line2D(lwpl_xs[i], lwpl_ys[i], linewidth=1, color='red'))

        #热度填充
        
        # 展示
        plt.plot()
        plt.savefig(self.path + '/heat.jpg',dpi = 100)
        print('保存为 '+self.path + '/heat.jpg')
