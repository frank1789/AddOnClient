#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows a tooltip on
a window and a button.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QRadioButton, QMessageBox


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def menuradiobutton(self):
        """Define menu with radio button, selectable one at time"""
        radio_install = QRadioButton("Install", self)
        radio_install.move(50, 25)
        radio_update = QRadioButton("Update", self)
        radio_update.move(50, 50)
        radio_remove = QRadioButton("Remove", self)
        radio_remove.move(50, 75)
        # connect signal and slot function
        radio_install.toggled.connect(self.radio_install_clicked)
        radio_update.toggled.connect(self.radio_update_clicked)
        radio_remove.toggled.connect(self.radio_remove_clicked)

    def initUI(self):
        # call menu radio button
        self.menuradiobutton()
        btn_exit = QPushButton("Exit", self)
        btn_exit.clicked.connect(self.close)
        btn_exit.move(200, 150)
        btn_next = QPushButton("Next", self)
        btn_next.move(135, 150)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Add-On Updater')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def addoninstall(self):
        QMessageBox.warning(self, 'Warning', "Function not avaiable!")

    def addonupdate(self):
        QMessageBox.warning(self, 'Warning', "Function not avaiable!")

    def addonremove(self):
        QMessageBox.warning(self, 'Warning', "Function not avaiable!")

    def radio_install_clicked(self, enabled):
        if enabled:
            self.addoninstall()

    def radio_update_clicked(self, enabled):
        if enabled:
            self.addonupdate()

    def radio_remove_clicked(self, enabled):
        if enabled:
            self.addonremove()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
