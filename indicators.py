import pandas as pd 
import numpy as np 
import csv
import util

import xlsxProc

class Indicators():

    traffic_day = []
    traffic_hour = []
    dict_store_name_id ={}
    dict_store_id_name ={}
    area = 0
    num_parking = 0
    duration = []
    dates = []

    def __init__(self,xlsxprocessor,inds,area_mainstore, duration):
        self.duration = duration
        self.dates = util.get_dates_within_duration(duration)
        self.traffic_day = xlsxprocessor.traffic_day.loc[self.dates,:]
        self.traffic_hour = xlsxprocessor.traffic_hour.loc[self.dates,:]
        self.dict_store_name_id = xlsxprocessor.dict_store_name_id
        self.dict_store_id_name = xlsxprocessor.dict_store_id_name
        self.mainstore = xlsxprocessor.mainstore
        self.area_mainstore = area_mainstore
        self.area = float(inds[0])
        self.num_parking = int(inds[1])

    
    '''def get_mainstore(self):
        return list(set([(id_.split('-')[0].split('F')[0],name) for id_, name  in self.dict_store_id_name.items() if ('-' in id_)]))
'''
    # 日均客流, 平日日均客流，周末日均客流
    def traffic_total_per_day(self):
        traffic_plaza_day = self.traffic_day.copy(deep = True)
        traffic_plaza_day = traffic_plaza_day['广场级']
        temp = [True if i.weekday()<4 else False for i in traffic_plaza_day.index]
        copy = traffic_plaza_day.copy(deep = True)
        traffic_plaza_day['weekday'] = temp
        temp = traffic_plaza_day.fillna(0).groupby(['weekday']).mean().sum(axis=1)
        try:
            weekday = temp[True]
        except:
            weekday = 0
        try:
            weekend = temp[False]
        except:
            weekend = 0
        return (copy.sum(axis = 1).mean(),weekday,weekend)

    '''def traffic_total_day(self):
        return self.traffic_day['广场级'].sum(axis = 1).mean()
    # 平日日均客流
    def traffic_total_weekday(self):
        return np.array([v for k, v in self.traffic_day['广场级'].sum(axis = 1).items() if (k.day_name()!='Friday' and k.day_name()!='Saturday' and k.day_name()!='Sunday')]).mean()

    # 周末日均客流
    def traffic_total_weekend(self):
        return np.array([v for k, v in self.traffic_day['广场级'].sum(axis = 1).items() if (k.day_name()!='Friday' or k.day_name()=='Saturday' or k.day_name()=='Sunday')]).mean()
    '''
    # 游逛深度
    def ratio_for_store(self):
        return self.traffic_day['店铺级'].sum(axis=1).mean() / self.traffic_total_per_day()[0]

    # 月均客流密度
    def density_month(self):
        return self.traffic_total_per_day()[0]/self.area*365/12

    # 日均车流, 平日日均车流，周末日均车流
    def traffic_car_per_day(self):
        traffic_park_day = self.traffic_day.copy(deep = True)
        traffic_park_day = traffic_park_day['停车场级']
        traffic_park_day = traffic_park_day.fillna(0)
        copy = traffic_park_day.copy(deep = True)
        temp = [True if i.weekday()<4 else False for i in traffic_park_day.index]
        traffic_park_day['weekday'] = temp
        temp = traffic_park_day.groupby(['weekday']).mean().sum(axis=1)
        try:
            weekday = temp[True]
        except:
            weekday = 0
        try:
            weekend = temp[False]
        except:
            weekend = 0
        return (copy.sum(axis = 1).mean(), weekday, weekend)
    
    # 车场使用频率
    def frequency_parking(self):
        return self.traffic_car_per_day()[0]/self.num_parking
    
    # 停车N入口日均车流
    def traffic_car_per_day_per_entry(self):
        traffic_park_day = self.traffic_day['停车场级']
        return traffic_park_day.mean(axis = 0)

    # N号主力店日均
    def traffic_per_day_per_mainstore(self):
        main_store = [name for _, name in self.mainstore]
        traffic_store_day = self.traffic_day['店铺级']
        return traffic_store_day.loc[:][main_store].mean(axis = 0)

    # N号主力店客流密度
    def density_mainstore(self):
        main_store = [name for _, name in self.mainstore]
        traffic_store_day = self.traffic_day['店铺级']
        return traffic_store_day.loc[:,main_store].sum(axis =0).div(np.array(self.area_mainstore))

    # 店铺日均
    def traffic_per_day_per_store(self):
        main_store = [name for _, name in self.mainstore]
        traffic_store_day = self.traffic_day['店铺级']
        return traffic_store_day.loc[:][[name for name in traffic_store_day.T.index if (name not in main_store)]].mean(axis = 0)


    # 楼层日均 与 楼层主力店贡献率
    def traffic_per_day_per_floor_and_ratio(self):
        traffic_store_day = self.traffic_day['店铺级']
        floor_store = [self.dict_store_name_id[name][0][:1] if self.dict_store_name_id[name][0][:2].isdigit() else self.dict_store_name_id[name][0][:2] for name in traffic_store_day.T.index]
        floor_store = [f.split('F')[0] for f in floor_store]
        traffic_floor_day = traffic_store_day.T
        traffic_floor_day['floor'] = floor_store
        main_store = [name for _, name in self.mainstore]
        temp1 = traffic_floor_day.groupby(['floor']).sum().mean(axis = 1)
        temp2 = traffic_floor_day.loc[main_store][:].groupby(['floor']).sum().mean(axis = 1)
        return (temp1, temp2.div(temp1))


    def write(self,path):
        out = []
        out.append(['日均客流'+'-'+'人次/天'])
        out.append(['',self.traffic_total_per_day()[0]])
        out.append(['平日日均客流'+'-'+'人次/天'])
        out.append(['',self.traffic_total_per_day()[1]])
        out.append(['周末日均客流'+'-'+'人次/天'])
        out.append(['',self.traffic_total_per_day()[2]])
        out.append(['游逛深度'+'-'+'个/人次'])
        out.append(['',self.ratio_for_store()])
        out.append(['月均客流密度'+'-'+'人次/月/㎡'])
        out.append(['',self.density_month()])

        out.append(['日均车流'+'-'+'车次/天'])
        out.append(['',self.traffic_car_per_day()[0]])
        out.append(['平日日均车流'+'-'+'车次/天'])
        out.append(['',self.traffic_car_per_day()[1]])
        out.append(['周末日均车流'+'-'+'车次/天'])
        out.append(['',self.traffic_car_per_day()[2]])
        out.append(['车场使用频率'+'-'+'次'])
        out.append(['',self.frequency_parking()])

        out.append(['停车场N入口日均车流'+'-'+'车次/天'])
        temp = self.traffic_car_per_day_per_entry()
        out += [['',i,v]for i,v in temp.items()]

        out.append(['主力店N日均'+'-'+'人次/天'])
        temp = self.traffic_per_day_per_mainstore()
        out += [['',i,v]for i,v in temp.items()]

        out.append(['主力店N客流密度'+'-'+'人/时段/平米'])
        temp = self.density_mainstore()
        out += [['',i,v]for i,v in temp.items()]

        out.append(['店铺日均'+'-'+'人次/天'])
        temp = self.traffic_per_day_per_store()
        out += [['',i,v]for i,v in temp.items()]

        out.append(['楼层日均'+'-'+'人次/天'])
        temp = self.traffic_per_day_per_floor_and_ratio()[0]
        out += [['',i,v]for i,v in temp.items()]

        out.append(['主力店楼层贡献率'+'-'+'%'])
        temp = self.traffic_per_day_per_floor_and_ratio()[1]
        out += [['',i,v*100]for i,v in temp.items()]

        with open(path,'w',newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(['指标','to'.join(self.duration)])
            f_csv.writerows(out)

if __name__=='__main__':
    xlsxprocessor = xlsxProc.xlsxProcessor('C:/Users/LuoZN/Desktop/客流数据/【客流+车场数据】0813.xlsx')
    indicators=Indicators(xlsxprocessor,['5000','300'],[1,1,1,1,1,1,1,1,1,1,1,1,1,1],('2019-03-01','2019-03-03'))
    indicators.write('./test1.csv')