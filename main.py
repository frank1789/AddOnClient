#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""AddOnManager
simple script to manage ElvUI from tukui.org

Author: Francesco Argentieri
Website: https://github.com/frank1789
Last edited: August 2018
"""

import sys
from PyQt5.QtWidgets import QApplication
from AddOnManager import MakeTitle, Example
from AddOnManager import Addonupdate as Addondownloader
from AddOnManager import Filemanager
from AddOnManager import PrintColour

if __name__ == '__main__':
    program_name = sys.argv[0]
    arguments = sys.argv[1:]
    count = len(arguments)
    print(arguments)
    if len(arguments) != 0:
        if arguments[0] == "-a" or arguments[0] == "-auto":
            # set local path
            addonfile = Filemanager()
            # check local version
            addonversion = Addondownloader()
            addonversion.checklocalversion(addonfile.getlocalfolder())
            # check remote version
            addonversion.checkremoteversion()
            if addonversion.getremoteversion() > addonversion.getlocalversion():
                print("Starting update...")
                addonfile.upgrade(addonversion.update())

            else:
                print(PrintColour("No new version").setfontstyle('blink'))

        elif arguments[0] == "-g" or arguments[0] == "--gui":
            app = QApplication(sys.argv)
            ex = Example()
            sys.exit(app.exec_())

    else:
        MakeTitle()

    # 4
    # addonfile.cleanup('/Users/francesco/PycharmProjects/AddOnClient/elvui-10.78.zip')
