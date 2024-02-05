import sys
import playsound
import threading
from PyQt5 import QtCore, QtGui, QtWidgets


class Keyboard(QtWidgets.QDialog):
    change_image_signal = QtCore.pyqtSignal(str)

    def __init__(self, dialog: QtWidgets.QDialog):
        """
        This class creates the onscreen keyboard GUI and logic, ready to be instansiated in main.py.
        :param dialog: QtWidgets.QDialog
        """
        super(Keyboard, self).__init__()
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
        dialog.setObjectName('Keyboard')
        self.window_x = 1440
        dialog.resize(self.window_x, 440)
        dialog.setMinimumSize(QtCore.QSize(self.window_x, 440))
        dialog.setMaximumSize(QtCore.QSize(self.window_x, 440))
        dialog.setStyleSheet('background-color: #BBF64D')

        x = 35
        space_1 = 76
        for i in range(1, self.white_num+1):
            white_button = QtWidgets.QPushButton(self.dialog)
            white_button.setGeometry(QtCore.QRect(x, 222, 70, 200))
            white_button.setStyleSheet(white_stylesheet)
            white_button.setObjectName(f'white_{i}')
            self.white_button_list.append(white_button)
            white_button.clicked.connect(self.make_on_click(white_button.objectName()))
            x += space_1

        counter = 0
        space_1, space_2, space_3 = 80, 140, 150
        x = 10
        for i in range(1, self.black_num+1):
            if x < self.window_x:
                counter += 1

                black_button = QtWidgets.QPushButton(self.dialog)
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
        dialog.setWindowTitle(_translate('Keyboard', 'Keyboard'))

        for white in enumerate(self.white_button_list):
            idx, button = white[0], white[1]
            text = self.white_note_list[idx % len(self.white_note_list)]
            button.setText(_translate('Keyboard', text))

        for black in enumerate(self.black_button_list):
            idx, button = black[0], black[1]
            text = self.black_note_list[idx % len(self.black_note_list)]
            button.setText(_translate('Keyboard', text))

        self.button_list = self.white_button_list + self.black_button_list
        self.button_list.sort(key=lambda b: b.pos().x())
        self.button_names_list = [b.objectName() for b in self.button_list]

    def make_on_click(self, note: str):
        """
        This function creates a function for each onscreen note pressed.
        :param note: string: button name
        :return: function: on_click
        """
        def on_click():
            threading.Thread(target=self.play_sound, args=(note,)).start()
            self.send_image_index(self.button_names_list.index(note))
        return on_click

    def play_sound(self, note: str) -> None:
        """
        Plays the note sound.
        :param note: string: button name
        :return:
        """
        playsound.playsound(f'sounds/{note}.mp3')

    def send_image_index(self, index) -> None:
        """
        Sends the image change signal to the main GUI class.
        :param index: int: note index
        :return:
        """
        self.change_image_signal.emit(str(index))


if __name__ == '__main__':
    # independently run script
    app = QtWidgets.QApplication(sys.argv)
    qt_dlg = QtWidgets.QDialog()
    Keyboard(qt_dlg)
    qt_dlg.show()
    app.exec_()
