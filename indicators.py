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

    def __init__(self,xlsxprocessor):
        self.traffic_day = xlsxprocessor.traffic_day
        self.traffic_hour = xlsxprocessor.traffic_hour
        self.dict_store_name_id = xlsxprocessor.dict_store_name_id
        self.dict_store_id_name = xlsxprocessor.dict_store_id_name
    
    def get_mainstore(self):
        return list(set([name for id_, name  in self.dict_store_id_name.items() if ('-' in id_)]))
    # 日均车流
    def traffic_car_per_day(self):
        return self.traffic_day['停车场级'].sum(axis =1).mean()
    # 平日日均车流，周末日均客流
    def traffic_car_per_day_weekday(self):
        traffic_park_day = self.traffic_day['停车场级']
        traffic_park_day['weekday']=[True if i.weekday()<4 else False for i in traffic_park_day.index]
        temp = traffic_park_day.fillna(0).groupby(['weekday']).mean().sum(axis=1)
        return (temp[True],temp[False])
    # 停车N入口日均车流
    def traffic_car_per_day_per_entry(self):
        traffic_park_day = self.traffic_day['停车场级']
        return traffic_park_day.mean()
    # N号主力店日均
    def traffic_per_day_per_mainstore(self):
        main_store = self.get_mainstore()
        traffic_store_day = self.traffic_day['店铺级']
        return traffic_store_day.loc[:][main_store].mean()
    # 楼层日均
    def traffic_per_day_per_floor(self):
        traffic_store_day = self.traffic_day['店铺级']
        floor_store = [self.dict_store_name_id[name][0][:1] if self.dict_store_name_id[name][0][:2].isdigit() else self.dict_store_name_id[name][0][:2] for name in traffic_store_day.T.index]
        traffic_floor_day = traffic_store_day.T
        traffic_floor_day['floor'] = floor_store
        main_store = self.get_mainstore()
        temp1 = traffic_floor_day.groupby(['floor']).sum().mean(axis = 1)
        temp2 = traffic_floor_day.loc[main_store][:].groupby(['floor']).sum().mean(axis = 1)
        return temp2.div(temp1)

    def write(self,path):
        out = []
        out.append(['日均车流'])
        out.append(['',self.traffic_car_per_day()])
        out.append(['平日日均车流'])
        out.append(['',self.traffic_car_per_day_weekday()[0]])
        out.append(['周末日均车流'])
        out.append(['',self.traffic_car_per_day_weekday()[1]])

        out.append(['停车场N入口日均车流'])
        temp = self.traffic_car_per_day_per_entry()
        out += [['',i,v]for i,v in zip(temp.index,temp)]

        out.append(['主力店N日均'])
        temp = self.traffic_per_day_per_mainstore()
        out += [['',i,v]for i,v in zip(temp.index,temp)]

        out.append(['楼层日均'])
        temp = self.traffic_per_day_per_floor()
        out += [['',i,v]for i,v in zip(temp.index,temp)]

        with open(path,'w',newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(['Indicators'])
            f_csv.writerows(out)

if __name__=='__main__':
    xlsxprocessor = xlsxProc.xlsxProcessor('C:/Users/LuoZN/Desktop/客流数据/【客流+车场数据】0813.xlsx')
    indicators=Indicators(xlsxprocessor)
    indicators.write('./test.csv')