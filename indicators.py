import pandas as pd 
import numpy as np 

import util

class Indicators():

    traffic_day = []
    traffic_hour = []
    dict_store_name_id ={}

    def __init__(self,xlsxprocessor):
        self.traffic_day = xlsxprocessor.traffic_day
        self.traffic_hour = xlsxprocessor.traffic_hour
        self.dict_store_name_id = xlsxprocessor.dict_store_name_id
    
    def 
