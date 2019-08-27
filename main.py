import sys
import os
import init
import util
import drawer

if __name__ =='__main__':

    initializer = init.Initializer()
    xlsx_processor = initializer.xlsx_processor
    dxf_processor = initializer.dxf_processor
    csv_processor = initializer.csv_processor

    current_path='/'.join(sys.path[0].split('\\'))
    heatdrawer = drawer.heatDrawer(current_path)
    heatdrawer.set_data(xlsx_processor,dxf_processor,csv_processor,initializer.date)
    output=heatdrawer.draw()
    os.startfile(output)