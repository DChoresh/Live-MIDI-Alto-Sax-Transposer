import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class GUI_transposer(QtWidgets.QDialog):
    def __init__(self, dialog):
        super(GUI_transposer, self).__init__()
        self.dialog = dialog
        dialog.setObjectName('Transposer')
        dialog.resize(1450, 440)
        dialog.setMinimumSize(QtCore.QSize(1450, 440))
        dialog.setMaximumSize(QtCore.QSize(1450, 440))
        dialog.setStyleSheet('background-color: #BBF64D')
        self.horizontalLayoutWidget = QtWidgets.QWidget(dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 200, 1364, 251))
        self.horizontalLayoutWidget.setObjectName('horizontalLayoutWidget')
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.white_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_1.setMinimumSize(QtCore.QSize(0, 200))
        self.white_1.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_1.setStyleSheet('background-color: #ffffff;\n'
                                   'font-size: 33pt;\n'
                                   'font-weight: bold;')
        self.white_1.setObjectName('white_1')
        self.horizontalLayout.addWidget(self.white_1)
        self.white_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_3.setMinimumSize(QtCore.QSize(0, 200))
        self.white_3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_3.setStyleSheet('background-color: #ffffff;\n'
                                   'font-size: 33pt;\n'
                                   'font-weight: bold;')
        self.white_3.setObjectName('white_3')
        self.horizontalLayout.addWidget(self.white_3)
        self.white_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_2.setMinimumSize(QtCore.QSize(0, 200))
        self.white_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_2.setStyleSheet('background-color: #ffffff;\n'
                                   'font-size: 33pt;\n'
                                   'font-weight: bold;')
        self.white_2.setObjectName('white_2')
        self.horizontalLayout.addWidget(self.white_2)
        self.white_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_4.setMinimumSize(QtCore.QSize(0, 200))
        self.white_4.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_4.setStyleSheet('background-color: #ffffff;\n'
                                   'font-size: 33pt;\n'
                                   'font-weight: bold;')
        self.white_4.setObjectName('white_4')
        self.horizontalLayout.addWidget(self.white_4)
        self.white_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_5.setMinimumSize(QtCore.QSize(0, 200))
        self.white_5.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_5.setStyleSheet('background-color: #ffffff;\n'
                                   'font-size: 33pt;\n'
                                   'font-weight: bold;')
        self.white_5.setObjectName('white_5')
        self.horizontalLayout.addWidget(self.white_5)
        self.white_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_6.setMinimumSize(QtCore.QSize(0, 200))
        self.white_6.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_6.setStyleSheet('background-color: #ffffff;\n'
                                   'font-size: 33pt;\n'
                                   'font-weight: bold;')
        self.white_6.setObjectName('white_6')
        self.horizontalLayout.addWidget(self.white_6)
        self.white_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_7.setMinimumSize(QtCore.QSize(0, 200))
        self.white_7.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_7.setStyleSheet('background-color: #e3ffb0;\n'
                                   'font-size: 33pt;\n'
                                   'font-weight: bold;')
        self.white_7.setObjectName('white_7')
        self.horizontalLayout.addWidget(self.white_7)
        self.white_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_8.setMinimumSize(QtCore.QSize(0, 200))
        self.white_8.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_8.setStyleSheet('background-color: #ffffff;\n'
                                   'font-size: 33pt;\n'
                                   'font-weight: bold;')
        self.white_8.setObjectName('white_8')
        self.horizontalLayout.addWidget(self.white_8)
        self.white_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_9.setMinimumSize(QtCore.QSize(0, 200))
        self.white_9.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_9.setStyleSheet('background-color: #ffffff;\n'
                                   'font-size: 33pt;\n'
                                   'font-weight: bold;')
        self.white_9.setObjectName('white_9')
        self.horizontalLayout.addWidget(self.white_9)
        self.white_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_10.setMinimumSize(QtCore.QSize(0, 200))
        self.white_10.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_10.setStyleSheet('background-color: #ffffff;\n'
                                    'font-size: 33pt;\n'
                                    'font-weight: bold;')
        self.white_10.setObjectName('white_10')
        self.horizontalLayout.addWidget(self.white_10)
        self.white_11 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_11.setMinimumSize(QtCore.QSize(0, 200))
        self.white_11.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_11.setStyleSheet('background-color: #ffffff;\n'
                                    'font-size: 33pt;\n'
                                    'font-weight: bold;')
        self.white_11.setObjectName('white_11')
        self.horizontalLayout.addWidget(self.white_11)
        self.white_12 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_12.setMinimumSize(QtCore.QSize(0, 200))
        self.white_12.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_12.setStyleSheet('background-color: #ffffff;\n'
                                    'font-size: 33pt;\n'
                                    'font-weight: bold;')
        self.white_12.setObjectName('white_12')
        self.horizontalLayout.addWidget(self.white_12)
        self.white_13 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_13.setMinimumSize(QtCore.QSize(0, 200))
        self.white_13.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_13.setStyleSheet('background-color: #ffffff;\n'
                                    'font-size: 33pt;\n'
                                    'font-weight: bold;')
        self.white_13.setObjectName('white_13')
        self.horizontalLayout.addWidget(self.white_13)
        self.white_14 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_14.setMinimumSize(QtCore.QSize(0, 200))
        self.white_14.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_14.setStyleSheet('background-color: #ffffff;\n'
                                    'font-size: 33pt;\n'
                                    'font-weight: bold;')
        self.white_14.setObjectName('white_14')
        self.horizontalLayout.addWidget(self.white_14)
        self.white_15 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_15.setMinimumSize(QtCore.QSize(0, 200))
        self.white_15.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_15.setStyleSheet('background-color: #ffffff;\n'
                                    'font-size: 33pt;\n'
                                    'font-weight: bold;')
        self.white_15.setObjectName('white_15')
        self.horizontalLayout.addWidget(self.white_15)
        self.white_16 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_16.setMinimumSize(QtCore.QSize(0, 200))
        self.white_16.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_16.setStyleSheet('background-color: #ffffff;\n'
                                    'font-size: 33pt;\n'
                                    'font-weight: bold;')
        self.white_16.setObjectName('white_16')
        self.horizontalLayout.addWidget(self.white_16)
        self.white_17 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_17.setMinimumSize(QtCore.QSize(0, 200))
        self.white_17.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_17.setStyleSheet('background-color: #ffffff;\n'
                                    'font-size: 33pt;\n'
                                    'font-weight: bold;')
        self.white_17.setObjectName('white_17')
        self.horizontalLayout.addWidget(self.white_17)
        self.white_18 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.white_18.setMinimumSize(QtCore.QSize(0, 200))
        self.white_18.setMaximumSize(QtCore.QSize(70, 16777215))
        self.white_18.setStyleSheet('background-color: #ffffff;\n'
                                    'font-size: 33pt;\n'
                                    'font-weight: bold;')
        self.white_18.setObjectName('white_18')
        self.horizontalLayout.addWidget(self.white_18)
        self.black_1 = QtWidgets.QPushButton(dialog)
        self.black_1.setGeometry(QtCore.QRect(10, 20, 60, 190))
        self.black_1.setMinimumSize(QtCore.QSize(0, 190))
        self.black_1.setMaximumSize(QtCore.QSize(60, 190))
        self.black_1.setStyleSheet('background-color: black;\n'
                                   'font-size: 23pt;\n'
                                   'font-weight: bold;\n'
                                   'color: white;')
        self.black_1.setObjectName('black_1')
        self.black_2 = QtWidgets.QPushButton(dialog)
        self.black_2.setGeometry(QtCore.QRect(90, 20, 60, 190))
        self.black_2.setMinimumSize(QtCore.QSize(0, 190))
        self.black_2.setMaximumSize(QtCore.QSize(60, 190))
        self.black_2.setStyleSheet('background-color: black;\n'
                                   'font-size: 23pt;\n'
                                   'font-weight: bold;\n'
                                   'color: white;')
        self.black_2.setObjectName('black_2')
        self.black_3 = QtWidgets.QPushButton(dialog)
        self.black_3.setGeometry(QtCore.QRect(230, 20, 60, 190))
        self.black_3.setMinimumSize(QtCore.QSize(0, 190))
        self.black_3.setMaximumSize(QtCore.QSize(60, 190))
        self.black_3.setStyleSheet('background-color: black;\n'
                                   'font-size: 23pt;\n'
                                   'font-weight: bold;\n'
                                   'color: white;')
        self.black_3.setObjectName('black_3')
        self.black_4 = QtWidgets.QPushButton(dialog)
        self.black_4.setGeometry(QtCore.QRect(310, 20, 60, 190))
        self.black_4.setMinimumSize(QtCore.QSize(0, 190))
        self.black_4.setMaximumSize(QtCore.QSize(60, 190))
        self.black_4.setStyleSheet('background-color: black;\n'
                                   'font-size: 23pt;\n'
                                   'font-weight: bold;\n'
                                   'color: white;')
        self.black_4.setObjectName('black_4')
        self.black_5 = QtWidgets.QPushButton(dialog)
        self.black_5.setGeometry(QtCore.QRect(390, 20, 60, 190))
        self.black_5.setMinimumSize(QtCore.QSize(0, 190))
        self.black_5.setMaximumSize(QtCore.QSize(60, 190))
        self.black_5.setStyleSheet('background-color: black;\n'
                                   'font-size: 23pt;\n'
                                   'font-weight: bold;\n'
                                   'color: white;')
        self.black_5.setObjectName('black_5')
        self.black_6 = QtWidgets.QPushButton(dialog)
        self.black_6.setGeometry(QtCore.QRect(540, 20, 60, 190))
        self.black_6.setMinimumSize(QtCore.QSize(0, 190))
        self.black_6.setMaximumSize(QtCore.QSize(60, 190))
        self.black_6.setStyleSheet('background-color: black;\n'
                                   'font-size: 23pt;\n'
                                   'font-weight: bold;\n'
                                   'color: white;')
        self.black_6.setObjectName('black_6')
        self.black_7 = QtWidgets.QPushButton(dialog)
        self.black_7.setGeometry(QtCore.QRect(620, 20, 60, 190))
        self.black_7.setMinimumSize(QtCore.QSize(0, 190))
        self.black_7.setMaximumSize(QtCore.QSize(60, 190))
        self.black_7.setStyleSheet('background-color: black;\n'
                                   'font-size: 23pt;\n'
                                   'font-weight: bold;\n'
                                   'color: white;')
        self.black_7.setObjectName('black_7')
        self.black_8 = QtWidgets.QPushButton(dialog)
        self.black_8.setGeometry(QtCore.QRect(760, 20, 60, 190))
        self.black_8.setMinimumSize(QtCore.QSize(0, 190))
        self.black_8.setMaximumSize(QtCore.QSize(60, 190))
        self.black_8.setStyleSheet('background-color: black;\n'
                                   'font-size: 23pt;\n'
                                   'font-weight: bold;\n'
                                   'color: white;')
        self.black_8.setObjectName('black_8')
        self.black_9 = QtWidgets.QPushButton(dialog)
        self.black_9.setGeometry(QtCore.QRect(840, 20, 60, 190))
        self.black_9.setMinimumSize(QtCore.QSize(0, 190))
        self.black_9.setMaximumSize(QtCore.QSize(60, 190))
        self.black_9.setStyleSheet('background-color: black;\n'
                                   'font-size: 23pt;\n'
                                   'font-weight: bold;\n'
                                   'color: white;')
        self.black_9.setObjectName('black_9')
        self.black_10 = QtWidgets.QPushButton(dialog)
        self.black_10.setGeometry(QtCore.QRect(920, 20, 60, 190))
        self.black_10.setMinimumSize(QtCore.QSize(0, 190))
        self.black_10.setMaximumSize(QtCore.QSize(60, 190))
        self.black_10.setStyleSheet('background-color: black;\n'
                                    'font-size: 23pt;\n'
                                    'font-weight: bold;\n'
                                    'color: white;')
        self.black_10.setObjectName('black_10')
        self.black_11 = QtWidgets.QPushButton(dialog)
        self.black_11.setGeometry(QtCore.QRect(1070, 20, 60, 190))
        self.black_11.setMinimumSize(QtCore.QSize(0, 190))
        self.black_11.setMaximumSize(QtCore.QSize(60, 190))
        self.black_11.setStyleSheet('background-color: black;\n'
                                    'font-size: 23pt;\n'
                                    'font-weight: bold;\n'
                                    'color: white;')
        self.black_11.setObjectName('black_11')
        self.black_12 = QtWidgets.QPushButton(dialog)
        self.black_12.setGeometry(QtCore.QRect(1150, 20, 60, 190))
        self.black_12.setMinimumSize(QtCore.QSize(0, 190))
        self.black_12.setMaximumSize(QtCore.QSize(60, 190))
        self.black_12.setStyleSheet('background-color: black;\n'
                                    'font-size: 23pt;\n'
                                    'font-weight: bold;\n'
                                    'color: white;')
        self.black_12.setObjectName('black_12')
        self.black_13 = QtWidgets.QPushButton(dialog)
        self.black_13.setGeometry(QtCore.QRect(1300, 20, 60, 190))
        self.black_13.setMinimumSize(QtCore.QSize(0, 190))
        self.black_13.setMaximumSize(QtCore.QSize(60, 190))
        self.black_13.setStyleSheet('background-color: black;\n'
                                    'font-size: 23pt;\n'
                                    'font-weight: bold;\n'
                                    'color: white;')
        self.black_13.setObjectName('black_13')
        self.black_14 = QtWidgets.QPushButton(dialog)
        self.black_14.setGeometry(QtCore.QRect(1380, 20, 60, 190))
        self.black_14.setMinimumSize(QtCore.QSize(0, 190))
        self.black_14.setMaximumSize(QtCore.QSize(60, 190))
        self.black_14.setStyleSheet('background-color: black;\n'
                                    'font-size: 23pt;\n'
                                    'font-weight: bold;\n'
                                    'color: white;')
        self.black_14.setObjectName('black_14')

        QtCore.QMetaObject.connectSlotsByName(dialog)
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate('Transposer', 'Transposer'))
        self.white_1.setText(_translate('Transposer', 'D'))
        self.white_3.setText(_translate('Transposer', 'E'))
        self.white_2.setText(_translate('Transposer', 'F'))
        self.white_4.setText(_translate('Transposer', 'G'))
        self.white_5.setText(_translate('Transposer', 'A'))
        self.white_6.setText(_translate('Transposer', 'B'))
        self.white_7.setText(_translate('Transposer', 'C'))
        self.white_8.setText(_translate('Transposer', 'D'))
        self.white_9.setText(_translate('Transposer', 'E'))
        self.white_10.setText(_translate('Transposer', 'F'))
        self.white_11.setText(_translate('Transposer', 'G'))
        self.white_12.setText(_translate('Transposer', 'A'))
        self.white_13.setText(_translate('Transposer', 'B'))
        self.white_14.setText(_translate('Transposer', 'C'))
        self.white_15.setText(_translate('Transposer', 'D'))
        self.white_16.setText(_translate('Transposer', 'E'))
        self.white_17.setText(_translate('Transposer', 'F'))
        self.white_18.setText(_translate('Transposer', 'G'))
        self.black_1.setText(_translate('Transposer', 'D♭'))
        self.black_2.setText(_translate('Transposer', 'E♭'))
        self.black_3.setText(_translate('Transposer', 'G♭'))
        self.black_4.setText(_translate('Transposer', 'A♭'))
        self.black_5.setText(_translate('Transposer', 'B♭'))
        self.black_6.setText(_translate('Transposer', 'D♭'))
        self.black_7.setText(_translate('Transposer', 'E♭'))
        self.black_8.setText(_translate('Transposer', 'G♭'))
        self.black_9.setText(_translate('Transposer', 'A♭'))
        self.black_10.setText(_translate('Transposer', 'B♭'))
        self.black_11.setText(_translate('Transposer', 'D♭'))
        self.black_12.setText(_translate('Transposer', 'E♭'))
        self.black_13.setText(_translate('Transposer', 'G♭'))
        self.black_14.setText(_translate('Transposer', 'A♭'))


app = QtWidgets.QApplication(sys.argv)
qt_dlg = QtWidgets.QDialog()
GUI_transposer(qt_dlg)
qt_dlg.show()
app.exec_()
