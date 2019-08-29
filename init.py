import xlsxProc, dxfProc, csvProc
import gui
import time

class Initializer():
    name_xlsx = './'
    name_dxf = './'
    name_csv = './'
    date = ''
    
    xlsx_processor=''
    dxf_processor=''
    csv_processor=''
        
    traffic_day = []
    traffic_hour = []
    dict_store_name_id = {}

    def __init__(self,filechooser):
        self.set_input(filechooser)
        self.process()

    def set_input(self,filechooser):
        
        self.name_xlsx = filechooser.name_file[0]
        self.name_dxf = filechooser.name_file[1]
        self.name_csv = filechooser.name_file[2]
        self.date = filechooser.date

    
    def process(self):
        time.sleep(2)
        print('proc start')
        print(self.name_xlsx,self.name_dxf, self.name_csv)

        self.xlsx_processor = xlsxProc.xlsxProcessor(self.name_xlsx)
        '''self.traffic_day = xlsx_processor.traffic_day
        self.traffic_hour = xlsx_processor.traffic_hour
        self.dict_store_id_name = xlsx_processor.dict_store_id_name'''
        self.dxf_processor = dxfProc.dxfProcessor(self.name_dxf)

        self.csv_processor = csvProc.csvProcessor(self.name_csv)

        print('proc stop')


if __name__ =='__main__':
    print('GUI start')
    filechooser = gui.fileChooser()
    print('GUI stop')
    initializer = Initializer(filechooser)
