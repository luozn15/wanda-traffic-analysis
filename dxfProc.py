import dxfgrabber
import math
from matplotlib.lines import Line2D
from matplotlib.patches import Arc
import matplotlib.pyplot as plt

class dxfProcessor():
    dxf_path = ''
    dxf = ''
    line = ''
    arc = ''
    ellipse = ''
    lwpline = ''
    xa, xi ,ya, yi =0, 0, 0, 0

    def __init__(self,dxf_path):
        print('dxfProcessor inited:')
        self.dxf = dxfgrabber.readfile(dxf_path)
        self.dxf_path = dxf_path
        self.line = self.get_line(self.dxf.entities)
        self.arc = self.get_arc(self.dxf.entities)
        self.ellipse = self.get_ellipse(self.dxf.entities)
        self.lwpline = self.get_lwpline(self.dxf.entities)

        self.xa, self.xi, self.ya, self.yi = self.set_boundary(self.line)
        print('dxfProcessor finished:')


    def get_line(self,entities):
        line=[]
        for e in entities:
            if e.dxftype=='LINE':
                line.append([e.start[:2], e.end[:2]])
        return line

    def get_arc(self,entities):
        arc = []
        for e in entities:
            if e.dxftype=='ARC':
                arc.append([e.center[:2],e.radius,e.start_angle,e.end_angle])
        return arc

    def get_ellipse(self,entities): 
        ellipse = []
        for e in entities:
            if e.dxftype=='ELLIPSE':
                center = e.center[:2]
                axis_major = e.major_axis[:2]
                radius_major = ((center[0]-axis_major[0])**2+(center[1]-axis_major[1])**2)**0.5
                radius_minor = e.ratio * radius_major
                angel = math.asin((axis_major[1]-center[1])/radius_major)/3.1415*360
                ellipse.append([center,radius_major,radius_minor,angel,e.start_param/3.1415*360,e.end_param/3.1415*360])
        return ellipse      

    def get_lwpline(self,entities): 
        lwpl = []
        for e in entities:
            if e.dxftype=='LWPOLYLINE':
                for i in range(len(e.points)-1):
                    pre=e.points[i]
                    nex=e.points[i+1]
                    bulge =e.bulge[i]
                    if bulge ==0:
                        lwpl.append([pre,nex])
                    else:
                        x_vec = nex[0] - pre[0]
                        y_vec = nex[1] - pre[1]
                        vec = (y_vec/(x_vec**2 + y_vec**2)**0.5*bulge,-x_vec/(x_vec**2 + y_vec**2)**0.5*bulge)
                        mid = ((pre[0] + nex[0])/2 + vec[0],(pre[1] + nex[1])/2 + vec[1])
                        lwpl.append([pre,mid])
                        lwpl.append([mid,nex])
                if e.is_closed ==True:
                    lwpl.append([e.points[-1],e.points[0]])
        return lwpl

    def set_boundary(self,line):
        x=[]
        y=[]
        for i in line:
            x1,y1 = i[0]
            x2,y2 = i[1]
            x+=[x1,x2]
            y+=[y1,y2]
        xa=max(x) 
        xi=min(x)
        ya=max(y)
        yi=min(y)
        #print(xa,xi,ya,yi)
        return (xa,xi,ya,yi)


if __name__ == '__main__':
    print('start')
    dxfprocessor = dxfProcessor('C:/Users/LuoZN/Desktop/客流数据/客流点位图.dxf')
    print('stop')
                