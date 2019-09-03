import xlsxProc, dxfProc, csvProc
import gui
import time
from multiprocessing import Process

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

    def P_xlsx(self,xlsx_processor,name_xlsx):
        print('xlsx begin')
        xlsx_processor = xlsxProc.xlsxProcessor(name_xlsx)
        print('xlsx finish')

    def P_dxf(self,dxf_processor,name_dxf):
        print('dxf begin')
        dxf_processor = dxfProc.dxfProcessor(name_dxf)
        print('dxf finish')

    def P_csv(self,csv_processor,name_csv):
        print('csv begin')
        csv_processor = csvProc.csvProcessor(name_csv)
        print('csv finish')

    def process(self):
        time.sleep(2)
        print('init start')
        print(self.name_xlsx,self.name_dxf, self.name_csv)

        '''self.xlsx_processor = xlsxProc.xlsxProcessor(self.name_xlsx)

        self.dxf_processor = dxfProc.dxfProcessor(self.name_dxf)

        self.csv_processor = csvProc.csvProcessor(self.name_csv)'''

        p_xlsx = Process(target = self.P_xlsx,args = (self.xlsx_processor,self.name_xlsx))
        p_dxf = Process(target = self.P_dxf,args = (self.dxf_processor,self.name_dxf))
        p_csv = Process(target = self.P_csv,args = (self.csv_processor,self.name_csv))

        p_xlsx.start()
        p_dxf.start()
        p_csv.start()
        p_xlsx.join()
        p_dxf.join()
        p_csv.join()

        print('init stop')


if __name__ =='__main__':
    print('GUI start')
    filechooser = gui.fileChooser()
    print('GUI stop')
    initializer = Initializer(filechooser)
