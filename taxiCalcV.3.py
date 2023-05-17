from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Create a web view
        self.web_view = QWebEngineView(self.centralwidget)
        self.web_view.setGeometry(QtCore.QRect(520, 0, 540, 640))
        
        self.dis = QtWidgets.QLineEdit(self.centralwidget)
        self.dis.setGeometry(QtCore.QRect(180, 60, 101, 20))
        self.dis.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dis.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dis.setDragEnabled(False)
        self.dis.setObjectName("dis")
        
        self.dis = QtWidgets.QLineEdit(self.centralwidget)
        self.dis.setGeometry(QtCore.QRect(180, 60, 101, 20))
        self.dis.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dis.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dis.setDragEnabled(False)
        self.dis.setObjectName("dis")
        
        self.timewait = QtWidgets.QLineEdit(self.centralwidget)
        self.timewait.setGeometry(QtCore.QRect(180, 90, 101, 20))
        self.timewait.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timewait.setObjectName("timewait")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 60, 60, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(105, 90, 70, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 170, 120, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 210, 81, 21))
        self.pushButton.setObjectName("pushButton")
        self.price = QtWidgets.QLabel(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(200, 180, 81, 20))
        self.price.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.price.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.price.setObjectName("price")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 60, 61, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 90, 51, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 180, 130, 21))
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 115, 90, 30))
        self.label_4.setObjectName("label_4")
        self.people = QtWidgets.QLineEdit(self.centralwidget)
        self.people.setGeometry(QtCore.QRect(180, 120, 101, 20))
        self.people.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.people.setObjectName("timewait_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(290, 120, 51, 21))
        self.label_10.setObjectName("label_10")
        self.hw = QtWidgets.QLabel(self.centralwidget)
        self.hw.setGeometry(QtCore.QRect(90, 150, 80, 21))
        self.hw.setObjectName("hw")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(180, 150, 101, 21))
        self.comboBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "คำนวนค่าเเท็กซี่"))
        self.label.setText(_translate("MainWindow", "ระยะทาง"))
        self.label_2.setText(_translate("MainWindow", "เวลารถติด"))
        self.label_3.setText(_translate("MainWindow", "ค่าโดยสาร(คนละ)"))
        self.pushButton.setText(_translate("MainWindow", "คำนวน"))
        self.price.setText(_translate("MainWindow", "0.00"))
        self.label_5.setText(_translate("MainWindow", "กิโลเมตร"))
        self.label_6.setText(_translate("MainWindow", "นาที"))
        self.label_7.setText(_translate("MainWindow", "บาท(โดยประมาณ)"))
        self.label_4.setText(_translate("MainWindow", "จำนวน"))
        self.label_10.setText(_translate("MainWindow", "คน"))
        self.hw.setText(_translate("MainWindow", "ขึ้นทางด่วน"))
        self.comboBox.setItemText(0, _translate("MainWindow", "ขึ้น"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ไม่ขึ้น"))
        self.pushButton.clicked.connect(self.calculate)
        # Initialize the map
        self.init_map()
    def init_map(self):
        url = QUrl("https://maps.google.com")
        self.web_view.load(url)    
    def calculate(self):
        dis=float(self.dis.text())
        timewait=float(self.timewait.text())
        people=int(self.people.text())
        hw=self.comboBox.currentText()
        #calculatepriceby dis
        if dis <= 1:
            price = 35.00
        elif dis <= 10:
            price = 35.00 + (dis - 1) * 6.50
        elif dis <= 20:
            price = 35.00 + (10 * 6.50) + (dis - 10) * 7.00
        elif dis <= 40:
            price = 35.00 + (10 * 6.50) + (10 * 7.00) + (dis - 20) * 8.00
        elif dis <= 60:
            price = 35.00 + (10 * 6.50) + (10 * 7.00) + (20 * 8.00) + (dis - 40) * 8.50
        elif dis <= 80:
            price = 35.00 + (10 * 6.50) + (10 * 7.00) + (20 * 8.00) + (20 * 8.50) + (dis - 60) * 9.00
        else:
            price = 35.00 + (10 * 6.50) + (10 * 7.00) + (20 * 8.00) + (20 * 8.50) + (20 * 9.00) + (dis - 80) * 10.50
        #calculatepriceby timewait
        timewait_charge=3.00*timewait
        #calculatepriceby if go on hightway
        if hw=="ขึ้น": 
            self.price.setText(str((price+timewait_charge+50)/people))
        else:self.price.setText(str((price+timewait_charge)/people))     

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
