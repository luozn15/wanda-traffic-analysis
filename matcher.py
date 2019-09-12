import dxfgrabber
import math
import numpy as np
import pandas as pd

class dxfProcesser_2():
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
        self.bounds = [[e.points[0], e.points[1]] for e in bounds]

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
        text=  ''.join(text.split('}'))
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
    '''ids_c = [[2160831.9051126 , 6157921.42193293],
       [2171431.30320349, 6158202.74277007],
       [2090676.27991509, 6130394.82632446],
       [2103559.13862518, 6129298.43946797],
       [2112618.17580785, 6129444.17675253],
       [2129014.36043283, 6131132.40109273],
       [2137493.54651533, 6130394.82632446],
       [2145204.90844321, 6128429.95462832],
       [2153894.21318127, 6128632.89032054],
       [2169180.07501517, 6130229.86811486],
       [2179102.69169268, 6130151.02907917],
       [2227745.99322079, 6158068.01925251],
       [2226501.88667955, 6165243.24140121],
       [2179730.62242895, 6213154.31437383]]
    bounds_c = [[2170693.11184272, 6159249.5193964 ],
       [2212254.39425503, 4990096.65852169],
       [2274451.02115907, 5371302.31422922],
       [2160203.0539122 , 6159229.98876968],
       [2154237.05098696, 6130751.73405989],
       [2169592.43535549, 6132014.7575332 ],
       [2178650.61962488, 6129472.3523403 ],
       [2103218.98864607, 6129386.70932359],
       [2112615.83819617, 6130332.61531669],
       [2134104.56093545, 6159241.56929285],
       [2120425.68273348, 6156023.71944962],
       [2179218.61743939, 6159249.08953484],
       [2196309.66664039, 6216260.23259896],
       [2194319.5568448 , 6173560.21002883]]'''
    
    mat = matcher('../客流点位图-F.dxf')
    print(mat.get_DF())