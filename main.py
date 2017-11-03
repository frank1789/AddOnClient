# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from AddOnManager import Maketitle
from AddOnManager import Addonupdate as Addondownloader
from AddOnManager import Filemanager

if __name__ == '__main__':
    Maketitle()

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
        print("No new version")

    sys.exit()
