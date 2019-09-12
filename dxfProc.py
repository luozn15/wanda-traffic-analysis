import dxfgrabber
import math
import numpy as np
import pandas as pd

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
        self.entities = [e for e in self.dxf.entities if (e.layer != 'ID' and e.layer !='Bounds')]
        self.line = self.get_line(self.entities)
        self.arc = self.get_arc(self.entities)
        self.ellipse = self.get_ellipse(self.entities)
        self.lwpline = self.get_lwpline(self.entities)

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

class dxfProcessor_2():
    dxf_path = '../客流点位图-F.dxf'
    dict_attachment_point = {   1:[-1,1], 
                                2:[0,1], 
                                3:[1,1],
                                4:[-1,0],
                                5:[0,0],
                                6:[1,0],
                                7:[-1,-1],
                                8:[0,-1],
                                9:[1,-1]    }
    ids = []
    bounds = []

    def __init__(self, dxf_path):
        self.dxf_path = dxf_path #'../客流点位图-F.dxf'
        dxf = dxfgrabber.readfile(self.dxf_path)
        ids = [e for e in dxf.entities if e.layer == 'ID' and (e.dxftype == 'TEXT' or e.dxftype == 'MTEXT')]
        bounds = [e for e in dxf.entities if e.layer == 'Bounds' and e.dxftype == 'LWPOLYLINE']
        self.bounds = np.array([e.points for e in bounds])

        self.ids_center = np.array([self.get_mtext_center(e,dxf.styles.get(e.style).width) if e.dxftype == 'MTEXT' else self.get_text_center(e) for e in ids])
        self.bounds_center = np.array([self.get_centerpoint(bound) for bound in bounds])
        self.ids_text = [self.get_text(e) for e in ids]


    def get_mtext_center(self, e, stylewidth):
        rows = np.array([len(line) for line in e.lines() if line != ''])
        x = rows.mean()/2 * stylewidth * e.height*0.8 #调试系数0.8
        lines = np.array([i for i,line in enumerate(e.lines()) if line != ''])
        y = (lines.mean()+0.5) * e.height*1.6 #调试系数1.6
        attach = self.dict_attachment_point[e.attachment_point]
        center_x = -x * attach[0]+e.insert[0]
        center_y = -y * attach[1]+e.insert[1]
        return center_x,center_y
    
    def get_text_center(self, e):
        height = e.height  
        center_x = e.align_point[0]
        center_y = e.align_point[1] + 0.5 * height
        return center_x,center_y
    
    def get_centerpoint(self, bound):
        area = 0.0
        x,y = 0.0,0.0   
        a = len(bound)
        for i in range(a):
            x0 = bound[i][0]
            y0 = bound[i][1]
            x1 = bound[i-1][0]
            y1 = bound[i-1][1]
            fg = (x0*y1 - x1*y0)/2.0
            area += fg
            x += fg*(x0+x1)/3.0
            y += fg*(y0+y1)/3.0  
        x = x/area
        y = y/area
        return x,y

    def get_text(self,e):
        text =  ''.join(e.lines()) if e.dxftype == 'MTEXT' else e.text 
        text = text.replace(' ', '')
        text = text.split(';')[-1]
        text = ''.join(text.split('}'))
        text = text.split('-')
        return text
    
    def get_content(self):
        return self.ids_center,  self.bounds_center, self.ids_text

    def match(self,ics,bcs):
        miniindex = []
        minidistance = []
        for i in range(len(ics)):
            ic = ics[i]
            distance = [abs(ic[0]-bc[0])+abs(ic[1]-bc[1]) for bc in bcs]
            index = distance.index(min(distance))
            dis = min(distance)
            if index in miniindex:
                i = miniindex.index(index)
                if minidistance[i] > dis:
                    miniindex[i] = -1
                    minidistance[i] = -1
                    miniindex.append(index)
                    minidistance.append(dis)
                else:
                    miniindex.append(-1)
                    minidistance.append(-1)
            else:
                miniindex.append(index)
                minidistance.append(dis)
        return miniindex
    
    def get_failed_index(self,miniindex):
        return [i for i,c in enumerate(miniindex) if c == -1]

    def get_DF(self):
        miniindex = self.match( self.ids_center, self.bounds_center)
        self.df = [[self.ids_text[i],self.bounds[j]] for i,j in enumerate(miniindex) if j != -1 ]
        self.df = pd.DataFrame(self.df, columns=['id','boundary'])
        return self.df

if __name__ == '__main__':
    print('start')
    dxfprocessor = dxfProcessor('C:/Users/LuoZN/Desktop/客流数据/客流点位图.dxf')
    print('stop')
                