import sys
import playsound
from PyQt5 import QtCore, QtGui, QtWidgets


class GUI_transposer(QtWidgets.QDialog):
    def __init__(self, dialog):
        super(GUI_transposer, self).__init__()
        self.dialog = dialog
        white_stylesheet = """
        background-color: #ffffff;
        font-size: 33pt;
        font-weight: bold;
        """
        black_stylesheet = """
        background-color: black;
        font-size: 23pt;
        font-weight: bold;
        color: white;
        """
        self.white_note_list = ['D', 'E', 'F', 'G', 'A', 'B', 'C']
        self.white_num = 18
        self.white_button_list = []
        self.black_note_list = ['D♭', 'E♭', 'G♭', 'A♭', 'B♭']
        self.black_num = 14
        self.black_button_list = []
        dialog.setObjectName('Transposer')
        self.window_x = 1440
        dialog.resize(self.window_x, 440)
        dialog.setMinimumSize(QtCore.QSize(self.window_x, 440))
        dialog.setMaximumSize(QtCore.QSize(self.window_x, 440))
        dialog.setStyleSheet('background-color: #BBF64D')
        self.horizontalLayoutWidget = QtWidgets.QWidget(dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 200, 1365, 250))
        self.horizontalLayoutWidget.setObjectName('horizontalLayoutWidget')
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName('horizontalLayout')

        for i in range(1, self.white_num+1):
            white_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            white_button.setMinimumSize(QtCore.QSize(70, 200))
            white_button.setStyleSheet(white_stylesheet)
            white_button.setObjectName(f'white_{i}')
            self.white_button_list.append(white_button)
            self.horizontalLayout.addWidget(white_button)
            white_button.clicked.connect(self.make_on_click(white_button.objectName()))

        counter = 0
        space_1, space_2, space_3 = 80, 140, 150
        x = 10
        for i in range(1, self.black_num+1):
            if x < self.window_x:
                counter += 1

                black_button = QtWidgets.QPushButton(dialog)
                black_button.setGeometry(QtCore.QRect(x, 20, 60, 190))
                black_button.setStyleSheet(black_stylesheet)
                black_button.setObjectName(f'black_{i}')
                self.black_button_list.append(black_button)
                black_button.clicked.connect(self.make_on_click(black_button.objectName()))

                if counter == 1 or 3 <= counter <= 4:
                    x += space_1
                elif counter == 2:
                    x += space_2
                elif counter == 5:
                    x += space_3
                    counter = 0

        QtCore.QMetaObject.connectSlotsByName(dialog)
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate('Transposer', 'Transposer'))

        for white in enumerate(self.white_button_list):
            idx, button = white[0], white[1]
            text = self.white_note_list[idx % len(self.white_note_list)]
            button.setText(_translate('Transposer', text))

        for black in enumerate(self.black_button_list):
            idx, button = black[0], black[1]
            text = self.black_note_list[idx % len(self.black_note_list)]
            button.setText(_translate('Transposer', text))

    def make_on_click(self, note):
        def on_click():
            playsound.playsound(f'sounds/{note}.mp3')
            print(note)
        return on_click


app = QtWidgets.QApplication(sys.argv)
qt_dlg = QtWidgets.QDialog()
GUI_transposer(qt_dlg)
qt_dlg.show()
app.exec_()
