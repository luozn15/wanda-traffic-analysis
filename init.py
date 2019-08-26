import matplotlib.pyplot as plt
import xlsxProc, dxfProc, csvProc
import gui
import time

class DataframeInitializer():
    name_xlsx = './'
    name_dxf = './'
    name_csv = './'
        
    traffic_day = []
    traffic_hour = []
    dict_store_name_id = {}

    def __init__(self):
        self.getInput()
        self.process()

    def getInput(self):
        print('GUI start')
        filechooser = gui.FileChooser()
        self.name_xlsx = filechooser.name_file[0]
        self.name_dxf = filechooser.name_file[1]
        self.name_csv = filechooser.name_file[2]
        print('GUI stop')
    
    def process(self):
        time.sleep(2)
        print('proc start')
        print(self.name_xlsx,self.name_csv)

        xlsx_processor = xlsxProc.xlsxProcessor(self.name_xlsx)
        self.traffic_day = xlsx_processor.traffic_day
        self.traffic_hour = xlsx_processor.traffic_hour
        self.dict_store_name_id = xlsx_processor.dict_store_name_id

        #dxf_processor = dxfProc.dxfProcessor(self.name_dxf, output_path)

        csv_processor = csvProc.csvProcessor(self.name_csv)

        print('proc stop')


if __name__ =='__main__':

    initializer = DataframeInitializer()
