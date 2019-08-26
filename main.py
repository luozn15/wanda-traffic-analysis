import init
import calculator
import drawer

if __name__ =='__main__':

    initializer = init.Initializer()
    dxf_processor = initializer.dxf_processor
    csv_processor = initializer.csv_processor
    heatdrawer = drawer.heatDrawer('.')
    heatdrawer.set_dxf(dxf_processor)
    heatdrawer.set_csv(csv_processor)
    heatdrawer.draw()