import matplotlib.pyplot as plt
import xlsxProc
import dwgProc
import gui
import time

class DataframeInitializer():
    name_xlsx = './'
    name_dwg = './'
        
    traffic_day = []
    traffic_hour = []
    dict_store_name_id = {}

    def __init__(self):
        self.getInput()
        self.process()

    def getInput(self):
        print('GUI start')
        filechooser = gui.FileChooser()
        self.name_xlsx = filechooser.name_xlsx
        self.name_dwg = filechooser.name_dwg
        print('GUI stop')
    
    def process(self):
        time.sleep(2)
        print('proc start')
        print(self.name_xlsx,self.name_dwg)

        xlsx_processor = xlsxProc.xlsxProcessor(self.name_xlsx)
        self.traffic_day = xlsx_processor.traffic_day
        self.traffic_hour = xlsx_processor.traffic_hour
        self.dict_store_name_id = xlsx_processor.dict_store_name_id

        dwg_processor = dwgProc.dwgProcessor(self.name_dwg)

        print('proc stop')


if __name__ =='__main__':

    initializer = DataframeInitializer()
