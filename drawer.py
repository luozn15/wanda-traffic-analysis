import math
import numpy as np
import pandas as pd
import matplotlib
from matplotlib.lines import Line2D
from matplotlib.patches import Arc,Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

import util

class heatDrawer():
    path = ''
    date = ''

    line = ''
    arc = ''
    ellipse = ''
    lwpline = ''
    xa, xi ,ya, yi =0, 0, 0, 0

    dxfprocessor =''
    csvprocessor =''
    xlsxprocessor =''
    df_store_heat = ''
    heat = ''

    def __init__(self,path):
        print('draw init')
        self.path = path

    def set_data(self,xlsxprocessor,dxfprocessor,csvprocessor,date):
        self.dxfprocessor = dxfprocessor
        self.csvprocessor =csvprocessor
        self.xlsxprocessor =xlsxprocessor
        self.date = date

    def get_df_store_heat(self):
        df_name_boundary = util.connect_name_boundary(self.csvprocessor,self.xlsxprocessor)
        df_store_heat = util.connect_store_traffic(df_name_boundary,self.xlsxprocessor)
        return df_store_heat

    def draw(self):
        xa = self.dxfprocessor.xa
        xi = self.dxfprocessor.xi
        ya = self.dxfprocessor.ya
        yi = self.dxfprocessor.yi
        line = self.dxfprocessor.line
        arc = self.dxfprocessor.arc
        ellipse = self.dxfprocessor.ellipse
        lwpline = self.dxfprocessor.lwpline
        print('draw begin')
        plt.clf()
        plt.close('all')
        figure, ax = plt.subplots(figsize=((xa-xi)/10000,(ya-yi)/10000), dpi=100)
        print('draw begin2')
        # 设置x，y值域
        ax.set_xlim(left=xi, right=xa,auto=False)
        ax.set_ylim(bottom=yi, top=ya,auto=False)

        # 底图绘制
        line_xs = [0]*len(line)
        line_ys = [0]*len(line)
        for i in range(len(line)):
            (line_xs[i], line_ys[i]) = zip(*line[i])

        for i in range(len(line_xs)):
            ax.add_line(Line2D(line_xs[i], line_ys[i], linewidth=1, color='black'))
            
        for i in arc:
            ax.add_patch(Arc(i[0], i[1], i[1], theta1= i[2], theta2=i[3]))
            
        for i in ellipse:
            ax.add_patch(Arc(i[0], i[1], i[2],angle = i[3], theta1= i[4], theta2=i[5]))
            
        lwpl_xs = [0]*len(lwpline)
        lwpl_ys = [0]*len(lwpline)
        for i in range(len(lwpline)):
            (lwpl_xs[i], lwpl_ys[i]) = zip(*lwpline[i])
        for i in range(len(lwpl_xs)):
            ax.add_line(Line2D(lwpl_xs[i], lwpl_ys[i], linewidth=1, color='black'))
        print('完成:底图绘制')

        #热度填充
        self.df_store_heat = self.get_df_store_heat()
        date = self.date
        self.heat = self.df_store_heat[pd.to_datetime(date)]

        boundaries = list(self.df_store_heat['boundary'])
        names = list(self.df_store_heat['name'])
        patches =[]
        for boundary ,name in zip(boundaries,names):
            center = util.get_center(boundary)
            polygon = Polygon(np.array(boundary), True)
            patches.append(polygon)
            plt.text(center[0],center[1],name)
        p = PatchCollection(patches, cmap = plt.get_cmap('rainbow') ,alpha=0.4)
        p.set_array(np.array(self.heat))
        p.set_clim([0,max(list(self.heat))])
        ax.add_collection(p)
        ax.set_aspect(1)
        figure.colorbar(p, ax=ax, orientation='horizontal')
        print('完成:热力绘制')

        # 展示
        plt.plot()
        plt.savefig(self.path + '/heat'+self.date+'.jpg',dpi = 100)
        
        #plt.show()
        print('保存为 '+self.path + '/heat'+self.date+'.jpg')
        return self.path + '/heat'+self.date+'.jpg'

class inputChecker():

    csvprocessor =''
    xlsxprocessor =''

    def __init__(self):
        pass

    def set_data(self,xlsxprocessor,csvprocessor):
        self.csvprocessor = csvprocessor
        self.xlsxprocessor =xlsxprocessor

    def get_num_null(self,traffic):
        num_null = list(traffic.isnull().sum(axis = 0))
        return num_null


    def get_figure(self):
        num_null_day = self.get_num_null(self.xlsxprocessor.traffic_day)
        num_null_hour = self.get_num_null(self.xlsxprocessor.traffic_hour)
        plt.cla()
        # 获取绘图并绘制
        self.fig = plt.figure(figsize=(1500,500))
        ax1 = self.fig.add_axes([0, 0, 1, 0.45])
        ax1.plot(num_null_day,'o--')
        ax2 = self.fig.add_axes([0, 0.5, 1, 0.45])
        ax2.plot(num_null_hour,'o--')
        plt.plot()
        return self.fig

    def close_fig(self):
        plt.close()
        plt.clf()