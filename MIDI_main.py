from time import sleep
import rtmidi
import os
import json
import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets


class MIDI_transcriber(QtWidgets.QDialog):
    show_popup_signal = QtCore.pyqtSignal(str)
    button_clicked_signal = QtCore.pyqtSignal()

    def __init__(self, dialog):
        super(MIDI_transcriber, self).__init__()
        self.dialog = dialog

        if not os.path.exists('devices'):
            os.makedirs('devices')

        self.setup_gui()
        midi_thread = threading.Thread(target=self.setup_midi_device, daemon=True)
        midi_thread.start()

        self.show_popup_signal.connect(self.popup)

    def setup_gui(self):
        self.dialog.setObjectName('MIDI_GUI')
        self.dialog.setWindowModality(QtCore.Qt.NonModal)
        self.dialog.setEnabled(True)
        self.dialog.resize(1099, 890)
        self.dialog.setMinimumSize(QtCore.QSize(1099, 890))
        self.dialog.setMaximumSize(QtCore.QSize(1099, 890))
        self.dialog.setAutoFillBackground(False)
        self.dialog.setStyleSheet('background: rgb(255, 255, 255)')
        self.grid_layout_widget = QtWidgets.QWidget(self.dialog)
        self.grid_layout_widget.setGeometry(QtCore.QRect(0, 0, 1113, 904))
        self.grid_layout_widget.setObjectName('gridLayoutWidget')
        self.grid_layout = QtWidgets.QGridLayout(self.grid_layout_widget)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setObjectName('gridLayout')
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item, 1, 0, 1, 1)
        self.pic_label = QtWidgets.QLabel(self.grid_layout_widget)
        self.pic_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pic_label.setText('')
        self.pic_label.setPixmap(QtGui.QPixmap('imgs/title.png'))
        self.pic_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_label.setObjectName('pic_label')
        self.grid_layout.addWidget(self.pic_label, 1, 1, 1, 1)
        spacer_item1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item1, 1, 2, 1, 1)
        spacer_item2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_layout.addItem(spacer_item2, 0, 1, 1, 1)
        spacer_item3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_layout.addItem(spacer_item3, 2, 1, 1, 1)
        _translate = QtCore.QCoreApplication.translate
        self.dialog.setWindowTitle(_translate('MIDI_GUI', 'Fingerings'))
        QtCore.QMetaObject.connectSlotsByName(self.dialog)

    def setup_midi_device(self):
        midi_in = rtmidi.MidiIn()
        self.devices_list = midi_in.get_ports()
        self.port = 'undefined'

        if len(self.devices_list) < 1:
            self.show_popup_signal.emit('no devices')
            sleep(10)
            os._exit(0)
        elif len(self.devices_list) == 1:
            self.port = 0
        elif len(self.devices_list) > 1:
            self.show_popup_signal.emit('multiple devices')
            loop = QtCore.QEventLoop()
            self.button_clicked_signal.connect(loop.quit)
            loop.exec_()

        self.midi_device = midi_in.open_port(int(self.port))
        self.device_name = self.devices_list[int(self.port)]

        if not os.path.exists(f'devices/{self.device_name}.json'):
            self.calibration()

        with open(f'devices/{self.device_name}.json', 'r') as f:
            config = json.load(f)

        self.key_on = config['key_on']
        self.key_off = config['key_off']
        self.range = [*range(config['Db3'], config['Db3']+32)]

        self.fingering_chart_printer()

    def calibration(self):
        self.show_popup_signal.emit('calibration')
        calib_msgs_list = []
        while len(calib_msgs_list) < 2:
            calib_msg = self.midi_device.get_message()
            if calib_msg is not None:
                calib_msgs_list.append(calib_msg)

        json_dict = {
            'key_on': calib_msgs_list[0][0][0],
            'key_off': calib_msgs_list[1][0][0],
            'Db3': calib_msgs_list[0][0][1] - 11
        }

        with open(f'devices/{self.device_name}.json', 'w') as f:
            json.dump(json_dict, f, indent=2, separators=(',', ': '))

        self.popup_window.close()

    @QtCore.pyqtSlot(str)
    def popup(self, mode):
        self.popup_window = QtWidgets.QDialog()
        popup_layout = QtWidgets.QVBoxLayout(self.popup_window)
        self.popup_window.setStyleSheet("background-color: #BBF64D")

        def add_title(text):
            title = QtWidgets.QLabel(text)
            title.setStyleSheet("font-weight: bold")
            popup_layout.addWidget(title)

        if mode == 'multiple devices':
            add_title('Multiple MIDI devices were detected, please select one.')

            for device in self.devices_list:
                button = QtWidgets.QPushButton(device)
                button.setStyleSheet("background-color: #d4fa8e")
                button.clicked.connect(self.make_on_click(device))
                popup_layout.addWidget(button)

        elif mode == 'no devices':
            add_title('No MIDI devices were detected, please connect one then relaunch.')

        elif mode == 'calibration':
            add_title('A new MIDI device was detected, please press the middle C to calibrate.')

        self.popup_window.exec_()

    def make_on_click(self, device):
        def on_click():
            self.port = self.devices_list.index(device)
            self.button_clicked_signal.emit()
            self.popup_window.close()
        return on_click

    def note_generator(self):
        while self.midi_device.is_port_open():
            msg = self.midi_device.get_message()
            if msg is not None:
                if msg[0][0] == self.key_on:
                    note_pressed = msg[0][1]
                    yield note_pressed

    def fingering_chart_printer(self):
        for note in self.note_generator():
            if note in self.range:
                self.pic_label.setPixmap(QtGui.QPixmap(f'imgs/{self.range.index(note)}.png'))
        return


app = QtWidgets.QApplication(sys.argv)
qt_dlg = QtWidgets.QDialog()
MIDI_transcriber(qt_dlg)
qt_dlg.show()
app.exec_()


