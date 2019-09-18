import sys
import os
import gui
import init
import util
import drawer
import indicators
import multiprocessing

def draw(xlsx_processor,dxf_processor,dxf_processor_2,date,path):
    heatdrawer = drawer.heatDrawer(path)
    heatdrawer.set_data(xlsx_processor,dxf_processor,dxf_processor_2,date)
    output=heatdrawer.draw()
    os.startfile(output)

if __name__ =='__main__':

    multiprocessing.freeze_support()
    print('GUI_filechooser start')
    filechooser = gui.fileChooser()
    print('GUI_filechooser stop')

    initializer = init.Initializer(filechooser)
    xlsx_processor = initializer.xlsx_processor
    dxf_processor = initializer.dxf_processor
    dxf_processor_2 = initializer.dxf_processor_2

    print('GUI_inputchecker start')
    inputchecker = gui.inputChecker(xlsx_processor.traffic_day, xlsx_processor.traffic_hour) 
    print('GUI_inputchecker stop')

    print('GUI_datechooser start')
    datechooser = gui.dateChooser(xlsx_processor.dates)
    duration = (datechooser.dates_chosen[0], datechooser.dates_chosen[-1])
    print('GUI_datechooser stop')

    #输入指标
    print('GUI_indicatorinput start')
    indicatorinput = gui.indicatorInput(xlsx_processor.mainstore)
    print('GUI_indicatorinput stop')

    indicators=indicators.Indicators(xlsx_processor, indicatorinput.inds, indicatorinput.area_mainstore, duration)
    indicators.write(indicatorinput.path)
    os.startfile(indicatorinput.path)
    img_path = os.path.split(indicatorinput.path)[0]
    #print(img_path)
    '''for date in datechooser.dates_chosen:
        print('main draw'+date)
        draw(xlsx_processor,dxf_processor,dxf_processor_2,date)'''
    
    draw(xlsx_processor,dxf_processor,dxf_processor_2,duration,img_path)

