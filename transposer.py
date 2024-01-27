from PyQt5 import QtCore, QtGui, QtWidgets
import playsound
import os


piano_scale_b = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
alto_scale_b = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
result = []


# noinspection PyUnresolvedReferences
class Ui_Transposer(object):
    def __init__(self, Transposer):
        Transposer.setObjectName("Transposer")
        Transposer.resize(699, 444)
        Transposer.setMinimumSize(QtCore.QSize(699, 444))
        Transposer.setMaximumSize(QtCore.QSize(699, 444))
        Transposer.setStyleSheet("background-color: #BBF64D")
        self.cButton = QtWidgets.QPushButton(Transposer)
        self.cButton.setGeometry(QtCore.QRect(40, 220, 81, 201))
        self.cButton.setStyleSheet("background-color: #ffffff;\n"
                                   "font-size: 33pt;\n"
                                   "font-weight: bold;")
        self.cButton.setObjectName("cButton")
        self.dButton = QtWidgets.QPushButton(Transposer)
        self.dButton.setGeometry(QtCore.QRect(130, 220, 81, 201))
        self.dButton.setStyleSheet("background-color: #ffffff;\n"
                                   "font-size: 33pt;\n"
                                   "font-weight: bold;")
        self.dButton.setObjectName("dButton")
        self.eButton = QtWidgets.QPushButton(Transposer)
        self.eButton.setGeometry(QtCore.QRect(220, 220, 81, 201))
        self.eButton.setStyleSheet("background-color: #ffffff;\n"
                                   "font-size: 33pt;\n"
                                   "font-weight: bold;")
        self.eButton.setObjectName("eButton")
        self.fButton = QtWidgets.QPushButton(Transposer)
        self.fButton.setGeometry(QtCore.QRect(310, 220, 81, 201))
        self.fButton.setStyleSheet("background-color: #ffffff;\n"
                                   "font-size: 33pt;\n"
                                   "font-weight: bold;")
        self.fButton.setObjectName("fButton")
        self.gButton = QtWidgets.QPushButton(Transposer)
        self.gButton.setGeometry(QtCore.QRect(400, 220, 81, 201))
        self.gButton.setStyleSheet("background-color: #ffffff;\n"
                                   "font-size: 33pt;\n"
                                   "font-weight: bold;")
        self.gButton.setObjectName("gButton")
        self.aButton = QtWidgets.QPushButton(Transposer)
        self.aButton.setGeometry(QtCore.QRect(490, 220, 81, 201))
        self.aButton.setStyleSheet("background-color: #ffffff;\n"
                                   "font-size: 33pt;\n"
                                   "font-weight: bold;")
        self.aButton.setObjectName("aButton")
        self.bButton = QtWidgets.QPushButton(Transposer)
        self.bButton.setGeometry(QtCore.QRect(580, 220, 81, 201))
        self.bButton.setStyleSheet("background-color: #ffffff;\n"
                                   "font-size: 33pt;\n"
                                   "font-weight: bold;")
        self.bButton.setObjectName("bButton")
        self.dbButton = QtWidgets.QPushButton(Transposer)
        self.dbButton.setGeometry(QtCore.QRect(90, 10, 71, 201))
        self.dbButton.setStyleSheet("background-color: #000000;\n"
                                    "font-size: 13pt;\n"
                                    "font-weight: bold;\n"
                                    "color: #ffffff;")
        self.dbButton.setObjectName("dbButton")
        self.ebButton = QtWidgets.QPushButton(Transposer)
        self.ebButton.setGeometry(QtCore.QRect(180, 10, 71, 201))
        self.ebButton.setStyleSheet("background-color: #000000;\n"
                                    "font-size: 13pt;\n"
                                    "font-weight: bold;\n"
                                    "color: #ffffff;")
        self.ebButton.setObjectName("ebButton")
        self.gbButton = QtWidgets.QPushButton(Transposer)
        self.gbButton.setGeometry(QtCore.QRect(360, 10, 71, 201))
        self.gbButton.setStyleSheet("background-color: #000000;\n"
                                    "font-size: 13pt;\n"
                                    "font-weight: bold;\n"
                                    "color: #ffffff;")
        self.gbButton.setObjectName("gbButton")
        self.abButton = QtWidgets.QPushButton(Transposer)
        self.abButton.setGeometry(QtCore.QRect(450, 10, 71, 201))
        self.abButton.setStyleSheet("background-color: #000000;\n"
                                    "font-size: 13pt;\n"
                                    "font-weight: bold;\n"
                                    "color: #ffffff;")
        self.abButton.setObjectName("abButton")
        self.bbButton = QtWidgets.QPushButton(Transposer)
        self.bbButton.setGeometry(QtCore.QRect(540, 10, 71, 201))
        self.bbButton.setStyleSheet("background-color: #000000;\n"
                                    "font-size: 13pt;\n"
                                    "font-weight: bold;\n"
                                    "color: #ffffff;")
        self.bbButton.setObjectName("bbButton")
        self.saveButton = QtWidgets.QPushButton(Transposer)
        self.saveButton.setGeometry(QtCore.QRect(10, 10, 31, 51))
        self.saveButton.setStyleSheet("background-color: #32a852;\n"
                                      "font_weight: bold;")
        self.saveButton.setObjectName("saveButton")
        self.delButton = QtWidgets.QPushButton(Transposer)
        self.delButton.setGeometry(QtCore.QRect(10, 69, 31, 51))
        self.delButton.setStyleSheet("background-color: #32a852;\n"
                                      "font_weight: bold;")
        self.delButton.setObjectName("delButton")

        self.cButton.clicked.connect(lambda: self._write_note('C'))
        self.dbButton.clicked.connect(lambda: self._write_note('Db'))
        self.dButton.clicked.connect(lambda: self._write_note('D'))
        self.ebButton.clicked.connect(lambda: self._write_note('Eb'))
        self.eButton.clicked.connect(lambda: self._write_note('E'))
        self.fButton.clicked.connect(lambda: self._write_note('F'))
        self.gbButton.clicked.connect(lambda: self._write_note('Gb'))
        self.gButton.clicked.connect(lambda: self._write_note('G'))
        self.abButton.clicked.connect(lambda: self._write_note('Ab'))
        self.aButton.clicked.connect(lambda: self._write_note('A'))
        self.bbButton.clicked.connect(lambda: self._write_note('Bb'))
        self.bButton.clicked.connect(lambda: self._write_note('B'))

        self.saveButton.clicked.connect(lambda: self._save())
        self.delButton.clicked.connect(lambda: self._delete_last())

        self.retranslateUi(Transposer)
        QtCore.QMetaObject.connectSlotsByName(Transposer)

    def retranslateUi(self, Transposer):
        _translate = QtCore.QCoreApplication.translate
        Transposer.setWindowTitle(_translate("Transposer", "Transposer"))
        self.cButton.setText(_translate("Transposer", "C"))
        self.dButton.setText(_translate("Transposer", "D"))
        self.eButton.setText(_translate("Transposer", "E"))
        self.fButton.setText(_translate("Transposer", "F"))
        self.gButton.setText(_translate("Transposer", "G"))
        self.aButton.setText(_translate("Transposer", "A"))
        self.bButton.setText(_translate("Transposer", "B"))
        self.dbButton.setText(_translate("Transposer", "C# / Db"))
        self.ebButton.setText(_translate("Transposer", "D# / Eb"))
        self.gbButton.setText(_translate("Transposer", "F# / Gb"))
        self.abButton.setText(_translate("Transposer", "G# / Ab"))
        self.bbButton.setText(_translate("Transposer", "A# / Bb"))
        self.saveButton.setText(_translate("Transposer", "save"))
        self.delButton.setText(_translate("Transposer", "⌫"))

    def _write_note(self, note):
        i = piano_scale_b.index(note)
        playsound.playsound(f'sounds/{i}.mp3')
        result.append(alto_scale_b[i])
        print(i, result)

    def _save(self):
        content_to_write = ','.join(result)
        with open('output.txt', 'w+') as f:
            f.write(content_to_write)
        exit()

    def _delete_last(self):
        result.pop()
        print(result)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    Ui_Transposer(dialog)
    dialog.show()
    app.exec_()
