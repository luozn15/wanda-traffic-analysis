from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import sip

class FileChooser(QtWidgets.QMainWindow):
    name_file = ['/'.join(sys.path[0].split('\\')[:-1]), '/'.join(sys.path[0].split('\\')[:-1]),'/'.join(sys.path[0].split('\\')[:-1])]#xlsx,dxf,csv
    date = ''
    file_type = ['Excel File (*.xlsx)','DXF File(*.dxf)','CSV File (*.csv)']
    status_list = ["选择xlsx文件","选择dxf文件","选择csv文件","选择日期"]
    instructions =  ["<h2>xlsx文件说明</h2> <p>1. 这里可以写一些说明</p> <p>2. 说明</p> <p>3. 这里可以写一些说明</p>",
                    "<h2>dxf文件说明</h2> <p>1. 这里可以写一些说明</p> <p>2. 说明</p> <p>3. 这里可以写一些说明</p>",
                    "<h2>csv文件说明</h2> <p>1. 这里可以写一些说明</p> <p>2. 说明</p> <p>3. 这里可以写一些说明</p>",
                    "<h2>选择日期说明</h2> <p>1. 格式 yyyy-mm-dd</p> <p>2. 如2018年12月1日为 2018-12-01</p> <p>3. 这里可以写一些说明</p>",
                    ]
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
        
        self.palette1 = QtGui.QPalette()
        #self.palette1.setColor(self.backgroundRole(), QtGui.QColor(192,253,123,200))   # 设置背景颜色
        self.palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('BingImageOfTheDay_20181030.jpg')))   # 设置背景图片
        #self.setPalette(self.palette1)



        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setObjectName('main_widget')
        


        self.top_widget = QtWidgets.QWidget()  # 创建上侧部件
        self.top_widget.setObjectName('top_widget')
        self.top_layout = QtWidgets.QGridLayout()  # 创建上侧部件的网格布局层
        self.top_widget.setLayout(self.top_layout) # 设置上侧部件布局为网格
        self.top_widget.setStyleSheet('''
                                        QWidget#top_widget{
                                            color:#333333;
                                            background:#fafafa;
                                            border-top:1px solid darkGray;
                                            border-left:1px solid darkGray;
                                            border-right:1px solid darkGray;
                                            border-top-left-radius:10px;
                                            border-top-right-radius:10px;
                                        }
                                    ''')

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QVBoxLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格
        self.left_widget.setStyleSheet('''
                                        QWidget#left_widget{
                                            color:#232C51;
                                            background:#eeeeee;
                                            border-top:1px solid darkGray;
                                            border-bottom:1px solid darkGray;
                                            border-left:1px solid darkGray;
                                            border-bottom-left-radius:10px;
                                            
                                        }
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
        #self.right_widget.setPalette(self.palette1)
        #self.right_widget.setAutoFillBackground(True)


        self.main_layout.addWidget(self.top_widget,     0,0,2,12) 

        self.main_layout.addWidget(self.left_widget,    2,0,8,3) # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget,   2,3,8,9) # 右侧部件在第0行第3列，占8行9列
        self.main_layout.setSpacing(0)
        self.setCentralWidget(self.main_widget) # 设置窗口主部件
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(0.99) # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        #self.setPalette(self.palette1)


        # top
        self.top_label_1 = QtWidgets.QLabel('客流分析')
        self.top_label_1.setFont(QtGui.QFont("黑体",20,QtGui.QFont.Bold))
        self.top_label_2 = QtWidgets.QLabel('版本  1')
        self.top_label_2.setFont(QtGui.QFont("黑体",15,QtGui.QFont.Normal))
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
        self.top_layout.addWidget(self.top_mini,        0,  blank,      1,  1)
        self.top_layout.addWidget(self.top_visit,       0,  blank+1,    1,  1)
        self.top_layout.addWidget(self.top_close,       0,  blank+2,    1,  1)
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
        self.right_text = QtWidgets.QTextEdit(self.instructions[self.status_id])
        self.right_text.setFocusPolicy(QtCore.Qt.NoFocus)
        self.right_text.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(100, 100, 100);")
        self.right_browser = QtWidgets.QPushButton('选择')
        self.right_browser.clicked.connect(self.popFileDialog)
        self.right_confirm = QtWidgets.QPushButton('确认')
        self.right_confirm.clicked.connect(self.confirm)
        self.right_file_input = QtWidgets.QLineEdit()
        self.right_file_input.setText(self.name_file[self.status_id])

        self.total_rows = 10
        self.total_columns = 10
        self.right_layout.addWidget(self.right_label_1,     0,              0,                  1,              1)
        self.right_layout.addWidget(self.right_text,        1,              0,                  self.total_rows-4,   self.total_columns)
        #self.right_layout.addWidget(QtWidgets.QLabel(),     self.total_rows-3,   0,                  1,              self.total_columns)
        self.right_layout.addWidget(self.right_file_input,  self.total_rows-2,   0,                  1,              self.total_columns-2)
        self.right_layout.addWidget(self.right_browser,     self.total_rows-2,   self.total_columns-2,    1,              1)
        self.right_layout.addWidget(self.right_confirm,     self.total_rows-2,   self.total_columns-1,    1,              1)
        
    def popFileDialog(self):     
        '''if self.status_id == 2 :
            self.close()'''
        filename = QtWidgets.QFileDialog.getOpenFileNames(self, self.status_list[self.status_id], self.name_file[self.status_id], self.file_type[self.status_id])[0]
        self.name_file[self.status_id] = filename[0] if len(filename)==1 else filename
        self.right_file_input.setText(' , '.join(filename))
    
    def confirm(self):
        self.status_id += 1
        if self.status_id < len(self.status_list)-1 : self.flash()
        elif self.status_id == len(self.status_list)-1: self.flash2()
        else : 
            self.date = self.right_date_input.text()
            self.close()
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
        self.right_text.setText(self.instructions[self.status_id])
        self.right_file_input.setText(self.name_file[self.status_id])

    def flash2(self):
        for i in range(len(self.left_label)):
            if i <= self.status_id:
                self.left_label[i].setStyleSheet("border:none;border-left:1px solid white;color:#ffffff;font-size:15px;font-weight:700;font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;")
            else:
                self.left_label[i].setStyleSheet("border:none;border-left:1px solid white;color:#999999;font-size:15px;font-weight:700;font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;")
        #right
        self.right_label_1.setText(self.status_list[self.status_id])
        self.right_text.setText(self.instructions[self.status_id])
        self.right_layout.removeWidget(self.right_file_input)
        self.right_layout.removeWidget(self.right_browser)
        sip.delete(self.right_file_input)
        sip.delete(self.right_browser)
        self.right_date_input = QtWidgets.QLineEdit()
        self.right_date_input.setPlaceholderText('yyyy-mm-dd')
        self.right_date_input.setInputMask('9999-99-99')
        self.right_layout.addWidget(self.right_date_input,  self.total_rows-2,   0,                  1,              self.total_columns-1)
        



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
    print(filechooser.date)
    print('stop')