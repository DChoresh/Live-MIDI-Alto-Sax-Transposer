import rtmidi
import os
import json
import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets


class MIDI_transcriber(object):
    def __init__(self, dialog):
        self.dialog = dialog

        if not os.path.exists('devices'):
            os.makedirs('devices')

        self.setup_gui()
        midi_thread = threading.Thread(target=self.setup_midi_device, daemon=True)
        midi_thread.start()

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
        devices_list = midi_in.get_ports()
        port = 0

        if len(devices_list) < 1:
            print('no midi devices available')
        elif len(devices_list) > 1:
            print('choose midi device:'
                  f'\n{devices_list}')
            port = input('port > ')

        self.midi_device = midi_in.open_port(int(port))
        self.device_name = devices_list[int(port)]
        print(f'device {self.device_name} selected')

        if not os.path.exists(f'devices/{self.device_name}.json'):
            self.calibration()

        with open(f'devices/{self.device_name}.json', 'r') as f:
            config = json.load(f)

        self.key_on = config['key_on']
        self.key_off = config['key_off']
        self.range = [*range(config['Db3'], config['Db3']+32)]

        self.fingering_chart_printer()

    def calibration(self):
        print('please press and release the middle C on your midi device')
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
                print(f'{note} - index/img {self.range.index(note)}')
                self.pic_label.setPixmap(QtGui.QPixmap(f'imgs/{self.range.index(note)}.png'))
        return


app = QtWidgets.QApplication(sys.argv)
qt_dlg = QtWidgets.QDialog()
MIDI_transcriber(qt_dlg)
qt_dlg.show()
app.exec_()


