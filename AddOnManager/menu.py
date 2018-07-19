# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


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
              "\n\tLicense: {!s}".format(self.__License), end='\n')

    def install(self):
        print ("You typed zero.\n")

    def update(self):
        print("n is a perfect square\n")

    def remove(self):
        print("n is an even number\n")



    def menu(self):
        print("1. Install", end='\n')
        print("2. Update", end='\n')
        print("3. Remove", end='\n')
        print("4. Exit", end='\n')
        while True:
            select = input("select: ")
            if int(select) == 1:
                 self.install()

            elif int(select) == 2:
                self.update()

            elif int(select) == 3:
                self.remove()

            elif int(select) == 4:
                sys.exit()

            else:
                print("wrong selection", end='\n')


if __name__ == '__main__':
     MakeTitle()
