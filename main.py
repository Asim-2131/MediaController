import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

       
        

class Ui_Form(object):

    def setupU(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 340, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 150, 141, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 240, 141, 51))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateU(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def mus(self):

        import music
    
    def vid(self):  

        import mediaplayer

    def dow(self):
         import download

    def retranslateU(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Video Player"))
        self.pushButton_2.setText(_translate("Form", "Music Player"))
        self.pushButton_3.setText(_translate("Form", "YT Downlod"))
        self.pushButton_2.clicked.connect(self.mus);
        self.pushButton.clicked.connect(self.vid);
        self.pushButton_3.clicked.connect(self.dow);



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupU(Form)
    Form.show()
    sys.exit(app.exec_())



