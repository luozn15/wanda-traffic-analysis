from multiprocessing import Process
import os

def P_xlsx(name_xlsx,return_dict):
        print('xlsx begin')
        xlsx_processor = name_xlsx
        return_dict['xlsx'] = xlsx_processor
        print('xlsx finish')

def P_dxf(name_dxf,return_dict):
        print('dxf begin')
        dxf_processor = name_dxf
        return_dict['dxf'] = dxf_processor
        print('dxf finish')

def P_csv(name_csv,return_dict):
        print('csv begin')
        csv_processor = name_csv
        return_dict['csv'] = csv_processor
        print('csv finish')

if __name__ == '__main__':
    return_dict = {}
    p1 = Process(target=P_xlsx, args=('bob',return_dict))
    p2 = Process(target=P_dxf, args=('anlo',return_dict))
    p3 = Process(target=P_csv, args=('cd',return_dict))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()
    print(return_dict)