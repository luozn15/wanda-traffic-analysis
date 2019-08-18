from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtCore import QCoreApplication
import sys

class FileChooser():
    name_xlsx = './'
    name_dwg = './'

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.w = QWidget()
        
        self.initUI()

        self.w.show()
        self.app.exec_()
    
    def initUI(self):
        self.w.resize(200, 450)
        self.w.move(300, 300)
        self.w.setWindowTitle('客流分析')

        lbl_xlsx = QLabel('请选择xlsx文件')
        hbox_xlsx = QHBoxLayout()
        hbox_xlsx.addStretch(1)
        hbox_xlsx.addWidget(lbl_xlsx)
        hbox_xlsx.addStretch(1)

        btn_xlsx = QPushButton('请选择xlsx文件', self.w)
        btn_xlsx.clicked.connect(self.popFileDialog)
        btn_xlsx.resize(btn_xlsx.sizeHint())

        lbl_dwg = QLabel('请选择dwg文件')
        hbox_dwg = QHBoxLayout()
        hbox_dwg.addStretch(1)
        hbox_dwg.addWidget(lbl_dwg)
        hbox_dwg.addStretch(1)

        btn_dwg = QPushButton('请选择dwg文件', self.w)
        btn_dwg.clicked.connect(self.popFileDialog)
        btn_dwg.resize(btn_dwg.sizeHint())

        btn_cfm = QPushButton('确认', self.w)
        btn_cfm.clicked.connect(self.w.close)

        vbox = QVBoxLayout()
        grid = QGridLayout()
        self.w.setLayout(vbox)  
        vbox.addStretch(1)
        vbox.addLayout(grid)

        grid.setSpacing(20)
        grid.addLayout(hbox_xlsx, 1,0)
        grid.addWidget(btn_xlsx, 2,0)
        grid.addLayout(hbox_dwg, 3,0)
        grid.addWidget(btn_dwg, 4,0)
        grid.addWidget(btn_cfm, 5,0)

    def popFileDialog(self):
        sender = self.w.sender().text()
        if sender == '请选择xlsx文件' :
            self.name_xlsx = QFileDialog.getOpenFileName(self.w, sender, self.name_xlsx, 'Excel File (*.xlsx)')[0]
        elif sender == '请选择dwg文件' :
            self.name_dwg = QFileDialog.getOpenFileName(self.w, sender, self.name_dwg, 'AutoCAD File (*.dwg)')[0]


if __name__ == '__main__':
    print('start')
    filechooser = FileChooser()
    print(filechooser.name_xlsx,filechooser.name_dwg)
    print('stop')