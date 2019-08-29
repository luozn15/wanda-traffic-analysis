import sys
import os
import gui
import init
import util
import drawer

if __name__ =='__main__':

    print('GUI_filechooser start')
    filechooser = gui.fileChooser()
    print('GUI_filechooser stop')

    initializer = init.Initializer(filechooser)
    xlsx_processor = initializer.xlsx_processor
    dxf_processor = initializer.dxf_processor
    csv_processor = initializer.csv_processor

    print('GUI_inputchecker start')
    inputchecker = gui.pltWindow(xlsx_processor,csv_processor)
    print('GUI_inputchecker stop')

    current_path='/'.join(sys.path[0].split('\\'))
    heatdrawer = drawer.heatDrawer(current_path)
    heatdrawer.set_data(xlsx_processor,dxf_processor,csv_processor,initializer.date)
    output=heatdrawer.draw()
    os.startfile(output)