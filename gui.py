from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class FileChooser(QtWidgets.QMainWindow):
    name_file = ['/'.join(sys.path[0].split('\\')[:-1]), '/'.join(sys.path[0].split('\\')[:-1])]#xlsx,csv
    file_type = ['Excel File (*.xlsx)','CSV File (*.csv)']
    status_list = ["选择xlsx文件","选择csv文件","确认输入文件","计算分析"]
    status_id = 0

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)

        super().__init__()
        self.initUI()
        self.show()
        app.exec_()

    def initUI(self):
        self.setFixedSize(800,500)
        self.move(300, 300)
        self.setWindowTitle('客流分析')


        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        


        self.top_widget = QtWidgets.QWidget()  # 创建上侧部件
        self.top_widget.setObjectName('top_widget')
        self.top_layout = QtWidgets.QGridLayout()  # 创建上侧部件的网格布局层
        self.top_widget.setLayout(self.top_layout) # 设置上侧部件布局为网格
        self.top_widget.setStyleSheet('''
                                        QWidget#top_widget{
                                            color:#333333;
                                            background:#eeeeee;
                                            border-top:1px solid darkGray;
                                            border-left:1px solid darkGray;
                                            border-right:1px solid darkGray;
                                            border-top-left-radius:10px;
                                            border-top-right-radius:10px;
                                        }
                                        QLabel#top_lable{
                                            border:none;
                                            font-size:16px;
                                            font-weight:700;
                                            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                                        }
                                    ''')

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QVBoxLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格
        self.left_widget.setStyleSheet('''
                                        QWidget#left_widget{
                                            color:#232C51;
                                            background:gray;

                                            border-bottom:1px solid darkGray;
                                            border-left:1px solid darkGray;
                                            border-bottom-left-radius:10px;
                                        }
                                        QLabel{border:none;color:white;}
                                        QLabel#left_label{
                                            border:none;
                                            border-left:1px solid white;
                                            font-size:15px;
                                            font-weight:700;
                                            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                                        }
                                    ''')

        self.right_widget = QtWidgets.QWidget() # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout) # 设置右侧部件布局为网格
        self.right_widget.setStyleSheet('''
                                        QWidget#right_widget{
                                            color:#232C51;
                                            background:white;
                                            border-top:1px solid darkGray;
                                            border-bottom:1px solid darkGray;
                                            border-right:1px solid darkGray;
                                            border-bottom-right-radius:10px;
                                        }
                                    ''')

        self.main_layout.addWidget(self.top_widget,     0,0,2,12) 
        self.main_layout.addWidget(self.left_widget,    2,0,8,3) # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget,   2,3,8,9) # 右侧部件在第0行第3列，占8行9列
        self.main_layout.setSpacing(0)
        self.setCentralWidget(self.main_widget) # 设置窗口主部件
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(0.99) # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明

        # top
        self.top_label_1 = QtWidgets.QLabel('客流分析')
        self.top_label_1.setFont(QtGui.QFont("黑体",30,QtGui.QFont.Bold))
        self.top_label_2 = QtWidgets.QLabel('版本  1')
        self.top_label_2.setFont(QtGui.QFont("黑体",15))
        self.top_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.top_visit = QtWidgets.QPushButton("") # 空白按钮
        self.top_close = QtWidgets.QPushButton("") # 关闭按钮
        self.top_mini.setFixedSize(15, 15) # 设置最小化按钮大小
        self.top_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.top_close.setFixedSize(15,15)
        self.top_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.top_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.top_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.top_mini.clicked.connect(self.showMinimized)
        self.top_visit.clicked.connect(self.showNormal)
        self.top_close.clicked.connect(self.close)

        blank = 15
        self.top_layout.addWidget(self.top_label_1,     0,  0,          1,  blank)
        self.top_layout.addWidget(self.top_label_2,     1,  0,          1,  blank)
        self.top_layout.addWidget(self.top_mini,       0,  blank,      1,  1)
        self.top_layout.addWidget(self.top_visit,       0,  blank+1,    1,  1)
        self.top_layout.addWidget(self.top_close,        0,  blank+2,    1,  1)
        self.top_layout.addWidget(QtWidgets.QLabel(''), 1,  0,          1,  blank+3)

        

        #left
        self.left_label=[]
        for i in range(len(self.status_list)):
            self.left_label.append(QtWidgets.QLabel(self.status_list[i]))#√-·
            self.left_label[i].setObjectName('left_label')
            if i <= self.status_id:
                self.left_label[i].setStyleSheet("border:none;border-left:1px solid white;color:#ffffff;font-size:15px;font-weight:700;font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;")
            else:
                self.left_label[i].setStyleSheet("border:none;border-left:1px solid white;color:#999999;font-size:15px;font-weight:700;font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;")
        
        self.left_label_5 = QtWidgets.QLabel("<p>copyright © WX_Studio 2019</p>")
        #self.left_label_5.setObjectName('left_label')

        self.left_layout.addWidget(QtWidgets.QLabel())
        for i in self.left_label:
            self.left_layout.addWidget(i)
        self.left_layout.addStretch(1)
        self.left_layout.addWidget(self.left_label_5)
        self.left_layout.setSpacing(20)

        #right
        self.right_label_1 = QtWidgets.QLabel()
        self.right_label_1.setText(self.status_list[self.status_id])
        self.right_label_1.setFont(QtGui.QFont("黑体",15,QtGui.QFont.Bold))
        self.right_text = QtWidgets.QTextEdit("<h2>xlsx文件说明</h2> \
                                                <p>1. 这里可以写一些说明</p> \
                                                <p>2. 说明</p> \
                                                <p>3. 这里可以写一些说明</p> \
                                                ")
        self.right_text.setFocusPolicy(QtCore.Qt.NoFocus)
        self.right_text.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(100, 100, 100);")
        self.right_browser = QtWidgets.QPushButton('选择')
        self.right_browser.clicked.connect(self.popFileDialog)
        self.right_confirm = QtWidgets.QPushButton('确认')
        self.right_confirm.clicked.connect(self.confirm)
        self.right_file_input = QtWidgets.QLineEdit()
        self.right_file_input.setText(self.name_file[self.status_id])

        total_rows = 10
        total_columns = 10
        self.right_layout.addWidget(self.right_label_1,     0,              0,                  1,              1)
        self.right_layout.addWidget(self.right_text,        1,              0,                  total_rows-4,   total_columns)
        #self.right_layout.addWidget(QtWidgets.QLabel(),     total_rows-3,   0,                  1,              total_columns)
        self.right_layout.addWidget(self.right_file_input,  total_rows-2,   0,                  1,              total_columns-2)
        self.right_layout.addWidget(self.right_browser,     total_rows-2,   total_columns-2,    1,              1)
        self.right_layout.addWidget(self.right_confirm,     total_rows-2,   total_columns-1,    1,              1)
        
        '''lbl_xlsx = QLabel('请选择xlsx文件')
        hbox_xlsx = QHBoxLayout()
        hbox_xlsx.addStretch(1)
        hbox_xlsx.addWidget(lbl_xlsx)
        hbox_xlsx.addStretch(1)

        btn_xlsx = QPushButton('请选择xlsx文件', self)
        btn_xlsx.clicked.connect(self.popFileDialog)
        btn_xlsx.resize(btn_xlsx.sizeHint())

        lbl_csv = QLabel('请选择csv文件')
        hbox_csv = QHBoxLayout()
        hbox_csv.addStretch(1)
        hbox_csv.addWidget(lbl_csv)
        hbox_csv.addStretch(1)

        btn_csv = QPushButton('请选择csv文件', self)
        btn_csv.clicked.connect(self.popFileDialog)
        btn_csv.resize(btn_csv.sizeHint())

        btn_cfm = QPushButton('确认', self)
        btn_cfm.clicked.connect(self.close)

        vbox = QVBoxLayout()
        grid = QGridLayout()
        self.setLayout(vbox)  
        vbox.addStretch(1)
        vbox.addLayout(grid)

        grid.setSpacing(20)
        grid.addLayout(hbox_xlsx, 1,0)
        grid.addWidget(btn_xlsx, 2,0)
        grid.addLayout(hbox_csv, 3,0)
        grid.addWidget(btn_csv, 4,0)
        grid.addWidget(btn_cfm, 5,0)'''

    def popFileDialog(self):     
        if self.status_id == 2 :
            self.close()
        self.name_file[self.status_id] = QtWidgets.QFileDialog.getOpenFileName(self, self.status_list[self.status_id], self.name_file[self.status_id], self.file_type[self.status_id])[0]
        self.right_file_input.setText(self.name_file[self.status_id])
    
    def confirm(self):
        self.status_id += 1
        if self.status_id > 1 : self.close()
        else: self.flash()
        print('confirm')
        
    def flash(self):
        #left
        for i in range(len(self.left_label)):
            if i <= self.status_id:
                self.left_label[i].setStyleSheet("border:none;border-left:1px solid white;color:#ffffff;font-size:15px;font-weight:700;font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;")
            else:
                self.left_label[i].setStyleSheet("border:none;border-left:1px solid white;color:#999999;font-size:15px;font-weight:700;font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;")
        #right
        self.right_label_1.setText(self.status_list[self.status_id])
        self.right_text.setText("<h2>又一个说明</h2> \
                                    <p>1. 这里可以写一些说明</p> \
                                    <p>2. 说明</p> \
                                    <p>3. 这里可以写一些说明</p> \
                                ")
        self.right_file_input.setText(self.name_file[self.status_id])

    def mousePressEvent(self, event):
        if event.button()==QtCore.Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            #self.setCursor(QtCore.QCursor(QtCore.Qt.OpenHandCursor))  #更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False

if __name__ == '__main__':
    print('start')
    filechooser = FileChooser()
    for i in filechooser.name_file:
        print(i)
    print('stop')