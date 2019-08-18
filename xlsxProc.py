import pandas as pd
import numpy as np

class xlsxProcessor():
    xlsx = ''
    traffic_day = []
    traffic_hour = []
    dict_store_name_id ={}

    def __init__(self,xlsx):
        print('xlsxProcessor inited:')
        self.xlsx = xlsx
        traffic_pathway_day = self.read_traffic_pathway_day()
        traffic_store_day, self.dict_store_name_id = self.read_traffic_store_day()
        traffic_entry_parking_day = self.read_traffic_entry_parking_day()

        self.traffic_day = pd.concat([traffic_pathway_day,traffic_store_day,traffic_entry_parking_day], axis=1)
        self.traffic_hour = self.read_traffic_hour()
        print(self.traffic_day.head(5),self.traffic_hour.head(5))

    def read_traffic_pathway_day(self):
        traffic_pathway_day = pd.read_excel(self.xlsx,'出入口及通道日客流数')
        name_pathway = list(traffic_pathway_day.iloc[0])[1:]
        traffic_pathway_day = traffic_pathway_day[2:]
        traffic_pathway_day['日期'] = pd.to_datetime(traffic_pathway_day['日期'])
        traffic_pathway_day = traffic_pathway_day.set_index('日期',drop = True)
        traffic_pathway_day.columns = [['广场级' for i in name_pathway],name_pathway]
        return traffic_pathway_day
    
    def read_traffic_store_day(self):
        traffic_store_day= pd.read_excel(self.xlsx,'店铺日客流量')
        name_store = list(traffic_store_day.iloc[0,1:])
        id_store = list(traffic_store_day.iloc[1,1:])
        id_store = [i.split(',') for i in id_store]
        dict_store_name_id = dict(zip(name_store,id_store))
        traffic_store_day = traffic_store_day[2:]
        traffic_store_day['日期'] = pd.to_datetime(traffic_store_day['日期'])
        traffic_store_day = traffic_store_day.set_index('日期',drop = True)
        traffic_store_day.columns =[['店铺级' for i in name_store],name_store]
        return (traffic_store_day, dict_store_name_id)

    def read_traffic_entry_parking_day(self):
        traffic_entry_parking_day= pd.read_excel(self.xlsx,'停车入口日客流量')
        name_entry_parking = list(traffic_entry_parking_day.iloc[0,1:])
        traffic_entry_parking_day = traffic_entry_parking_day[2:]
        traffic_entry_parking_day['日期'] = pd.to_datetime(traffic_entry_parking_day['日期'])
        traffic_entry_parking_day = traffic_entry_parking_day.set_index('日期',drop = True)
        traffic_entry_parking_day.columns = [['停车场级' for i in name_entry_parking],name_entry_parking]
        return traffic_entry_parking_day

    def read_traffic_hour(self):
        traffic_hour = pd.read_excel(self.xlsx,'分时段客流数')
        temp = list(traffic_hour['日期'])[2:]
        date =[]
        for i in temp:
            if i == i: date.append(i)
            else: date.append(date[-1])

        time = list(traffic_hour['时段'])[2:]

        temp = list(traffic_hour.columns)[2:]
        level =[]
        for i in temp:
            if i[:7]=='Unnamed': level.append(level[-1])
            else: level.append(i)

        name = list(traffic_hour.iloc[0,2:])

        traffic_hour = traffic_hour.iloc[2:,2:]
        traffic_hour =traffic_hour.set_index([date,time])
        traffic_hour.columns = [level,name]

        return traffic_hour