#

from PyQt5 import QtCore, QtGui, QtWidgets
from CNN import build
from Prediction import Ui_Detection
import sys
class Ui_AdminHome(object):

    def cnnbuild(self):
        try:
            build();
            self.showMessageBox("Message", "CNN build successfully.")

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
    def detect(self):

        try:
            self.admn = QtWidgets.QDialog()
            self.ui = Ui_Detection()
            self.ui.setupUi(self.admn)
            self.admn.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def showMessageBox(self, title, message):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setWindowTitle(title)
            msgBox.setText(message)
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 447)
        Dialog.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-70, 0, 841, 471))
        self.label.setStyleSheet("image: url(../Detection/images/bg6.jpg);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 100, 241, 51))
        self.pushButton.setStyleSheet("background-color: rgb(170, 85, 0);\n"
"font: 12pt \"Franklin Gothic Heavy\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.cnnbuild)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 220, 241, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 85, 0);\n"
"font: 12pt \"Franklin Gothic Heavy\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.detect)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Abnormal activity detection using CNN"))
        self.label.setText(_translate("Dialog", ""))
        self.pushButton.setText(_translate("Dialog", "Build CNN Model"))
        self.pushButton_2.setText(_translate("Dialog", "Object Detection"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_AdminHome()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
