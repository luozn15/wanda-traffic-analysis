import xlsxProc, dxfProc
import gui
import time
from multiprocessing import Pool

class Initializer():
    name_xlsx = './'
    name_dxf = './'
    #name_csv = './'
    date = ''
    
    xlsx_processor=''
    dxf_processor=''
    dxf_processor_2=''
        
    traffic_day = []
    traffic_hour = []
    dict_store_name_id = {}

    def __init__(self,filechooser):
        self.set_input(filechooser)
        self.process()

    def set_input(self,filechooser):
        
        self.name_xlsx = filechooser.name_file[0]
        self.name_dxf = filechooser.name_file[1]
        #self.name_csv = filechooser.name_file[2]
        self.date = filechooser.date

    def P_xlsx(self,name_xlsx):
        xlsx_processor = xlsxProc.xlsxProcessor(name_xlsx)
        return xlsx_processor

    def P_dxf(self,name_dxf):
        dxf_processor = dxfProc.dxfProcessor(name_dxf)
        return dxf_processor

    def P_dxf_2(self,name_dxf):
        dxf_processor_2 = dxfProc.dxfProcessor_2(name_dxf)
        return dxf_processor_2

    def process(self):
        time.sleep(2)
        print('init start')
        time_start=time.time()
        
        '''self.xlsx_processor = xlsxProc.xlsxProcessor(self.name_xlsx)
        self.dxf_processor = dxfProc.dxfProcessor(self.name_dxf)
        self.dxf_processor_2 = dxfProc.dxfProcessor_2(self.name_dxf)'''

        pool = Pool(3)

        self.xlsx_processor = pool.map(self.P_xlsx,(self.name_xlsx,))[0]
        self.dxf_processor = pool.map(self.P_dxf,(self.name_dxf,))[0]
        self.dxf_processor_2 = pool.map(self.P_dxf_2,(self.name_dxf,))[0]

        pool.close()
        pool.join()

        time_end=time.time()
        print('init stop with time_cost:',time_end-time_start,'s')
        

if __name__ =='__main__':
    print('GUI start')
    filechooser = gui.fileChooser()
    print('GUI stop')
    initializer = Initializer(filechooser)
