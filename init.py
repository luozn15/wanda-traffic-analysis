import xlsxProc, dxfProc, csvProc
import gui
import time
from multiprocessing import Pool

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

    def P_xlsx(self,name_xlsx):
        xlsx_processor = xlsxProc.xlsxProcessor(name_xlsx)
        return xlsx_processor

    def P_dxf(self,name_dxf):
        dxf_processor = dxfProc.dxfProcessor(name_dxf)
        return dxf_processor

    def P_csv(self,name_csv):
        csv_processor = csvProc.csvProcessor(name_csv)
        return csv_processor

    def process(self):
        time.sleep(2)
        print('init start')
        #print(self.name_xlsx,self.name_dxf, self.name_csv)

        '''self.xlsx_processor = xlsxProc.xlsxProcessor(self.name_xlsx)

        self.dxf_processor = dxfProc.dxfProcessor(self.name_dxf)

        self.csv_processor = csvProc.csvProcessor(self.name_csv)'''
        pool = Pool(3)

        self.xlsx_processor = pool.map(self.P_xlsx,(self.name_xlsx,))[0]
        self.dxf_processor = pool.map(self.P_dxf,(self.name_dxf,))[0]
        self.csv_processor = pool.map(self.P_csv,(self.name_csv,))[0]

        '''p_xlsx.start()
        p_dxf.start()
        p_csv.start()
        p_xlsx.join()
        p_dxf.join()
        p_csv.join()'''
        #print('xlsx',self.xlsx_processor.xlsx)
        #print('dxf',self.dxf_processor.dxf)
        #print('csv',self.csv_processor.csv)
        pool.close()
        pool.join()
        print('init stop')

if __name__ =='__main__':
    print('GUI start')
    filechooser = gui.fileChooser()
    print('GUI stop')
    initializer = Initializer(filechooser)
