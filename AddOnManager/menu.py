# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from .Addonupdate import Addonupdate as Addondownloader
from .Filemanager import Filemanager
from .colour import PrintColour


class MakeTitle:
    __name = "Francesco"
    __surname = "Argentieri"
    __License = "MIT"

    def __init__(self):
        self.title()
        self.information()
        self.menu()

    def title(self):
        # print text art ascii title
        print("___________.__        ____ ___.___     _____       .___  .___________\n"
              "\_   _____/|  |___  _|    |   \   |   /  _  \    __| _/__| _/\_____  \   ____ \n"
              " |    __)_ |  |\  \/ /    |   /   |  /  /_\  \  / __ |/ __ |  /   |   \ /    \ \n"
              " |        \|  |_\   /|    |  /|   | /    |    \/ /_/ / /_/ | /    |    \   |  \ \n"
              "/_______  /|____/\_/ |______/ |___| \____|__  /\____ \____ | \_______  /___|  /\n"
              "        \/                                  \/      \/    \/         \/     \/ ")
        print("\t\t\t ____ ____ ____ ____ ____ ____\n"
              "\t\t\t||u |||p |||d |||a |||t |||e ||\n"
              "\t\t\t||__|||__|||__|||__|||__|||__||\n"
              "\t\t\t|/__\|/__\|/__\|/__\|/__\|/__\|\n")

    def information(self):
        # print information from git
        print("\tVersion {}".format(0),
              "\t\tAuthor: {!s}".format(self.__name + " " + self.__surname),
              "\n\tLicense: {!s}".format(self.__License), end='\n\n')

    def install(self):
        print("You typed zero.\n")

    def update(self):
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

    def remove(self):
        print("n is an even number\n")

    def menu(self):
        print("1. Install", end='\n')
        print("2. Update", end='\n')
        print("3. Remove", end='\n')
        print("4. Exit", end='\n\n')
        while True:
            select = input("\tSelect: ")
            try:
                checked_select = int(select)
                if int(checked_select) == 1:
                    self.install()

                elif int(checked_select) == 2:
                    self.update()
                    checked_select = 4
                    return checked_select

                elif int(checked_select) == 3:
                    checked_select = 4
                    return checked_select

                elif int(checked_select) == 4:
                    sys.exit()

                else:
                    print('\t"{}" is not valid selection'.format(checked_select), end='\n')

            except ValueError:
                print('\t"{}" is not a number. Try again.'.format(select))


if __name__ == '__main__':
    MakeTitle()
