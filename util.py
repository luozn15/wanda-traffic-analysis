import pandas as pd
import numpy as np

def connect_name_boundary(csvprocessor, xlsxprocessor):
    csv = csvprocessor.csv
    dict_store_name_id = xlsxprocessor.dict_store_name_id

    dict_store_id_name={}
    for name,ids in dict_store_name_id.items() :
        for id_ in ids:
            dict_store_id_name[id_]=name

    store_name= []
    for i in list(csv['id']):
        try:
            print(dict_store_id_name[i[0]])
            store_name.append(dict_store_id_name[i[0]])
        except:
            print(i[0])
            store_name.append(i[0])
    df_name_boundary = csv.copy()
    df_name_boundary['name'] = store_name
    print('connect_name_boundary')
    return df_name_boundary

def connect_store_traffic(df_name_boundary,xlsxprocessor):
    store_name = df_name_boundary['name']
    traffic_store_day = xlsxprocessor.traffic_day['店铺级']
    traffic = df_name_boundary
    for i in range(len(traffic_store_day)):
        traffic_store=[]
        for name in store_name:
            try:
                traffic_store.append(traffic_store_day.iloc[i][name])
            except:
                traffic_store.append(0)
        
        traffic[traffic_store_day.index[i]]=traffic_store
    print('connect_store_traffic')
    return traffic

def get_center(boundary):
    xs=0
    ys=0
    for x, y in boundary:
        xs+=x
        ys+=y
    return (xs/len(boundary),ys/len(boundary))
