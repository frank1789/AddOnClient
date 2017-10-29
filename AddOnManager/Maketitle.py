# !/usr/bin/python3
# -*- coding: utf-8 -*-


class Maketitle:
    __name = "Francesco"
    __surname = "Argentieri"
    __License = "MIT"

    def __init__(self):
        self.title()
        self.information()

    @staticmethod
    def title():
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
