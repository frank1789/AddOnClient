# !/usr/bin/python3
# -*- coding: utf-8 -*-


from AddOnManager import Maketitle
from AddOnManager import Addonupdate as Addondownloader

if __name__ == '__main__':
    Maketitle()

    # set local path #todo modificare con ricerca nella classe manager file
    localpath = "/Applications/World of Warcraft/Interface/AddOns/ElvUI/"

    # check the version
    addon = Addondownloader()
    addon.checklocalversion(localpath)

    # now check the remote version
    addon.checkremoteversion()
    if addon.getremoteversion() > addon.getlocalversion():
        addon.update()

    else:
        print("No new version!")
