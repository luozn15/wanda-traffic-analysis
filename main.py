import sys
import os
import gui
import init
import util
import drawer
import indicators

def draw(xlsx_processor,dxf_processor,csv_processor,date):
    current_path='/'.join(sys.path[0].split('\\'))
    heatdrawer = drawer.heatDrawer(current_path)
    heatdrawer.set_data(xlsx_processor,dxf_processor,csv_processor,date)
    output=heatdrawer.draw()
    os.startfile(output)

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

    print('GUI_datechooser start')
    datechooser = gui.dateChooser(xlsx_processor)
    print('GUI_datechooser stop')

    indicators=indicators.Indicators(xlsx_processor)
    indicators.write('./test.csv')

    for date in datechooser.dates_chosen:
        print('main draw'+date)
        draw(xlsx_processor,dxf_processor,csv_processor,date)

