# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from AddOnManager import MakeTitle
from AddOnManager import Addonupdate as Addondownloader
from AddOnManager import Filemanager
from AddOnManager import PrintColour

if __name__ == '__main__':
    program_name = sys.argv[0]
    arguments = sys.argv[1:]
    count = len(arguments)
    print(arguments)
    if len(arguments) != 0 and arguments[0] == "-a":
        # set local path
        addonfile = Filemanager()

        # check the version
        addonversion = Addondownloader()
        addonversion.checklocalversion(addonfile.getlocalfolder())

        # check the remote version
        addonversion.checkremoteversion()
        if addonversion.getremoteversion() > addonversion.getlocalversion():
            print("Starting update...")
            addonfile.upgrade(addonversion.update())

        else:
            print(PrintColour("No new version").setfontstyle('blink'))




    else:
        MakeTitle()


    #addonfile.cleanup('/Users/francesco/PycharmProjects/AddOnClient/elvui-10.78.zip')

    sys.exit()
