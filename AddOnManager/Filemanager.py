# !/usr/bin/python3
# -*- coding: utf-8 -*-


import os
from .Addonupdate import PrintColour
import zipfile as zip
from send2trash import send2trash


class Filemanager:
    # folder where store the add-on of WOW, as
    __PATH = '/Applications/World of Warcraft/Interface/AddOns'  # changeless

    def __init__(self):
        self.setlocalfolder()

    def setlocalfolder(self):
        """
        search files with ".toc" extension in predefined folder

        """
        for root, dirs, files in os.walk(self.__PATH):
            for file in files:
                # make string of path
                if file.endswith(".toc"):
                    # print(os.path.join(root, file), end='\n')  # enable for debug
                    keyword = 'ElvUI.toc'
                    if keyword in os.path.join(root, file):
                        self.local_path = os.path.join(root, file)
                        # print("success:", self.__local_path) # enable for debug

        print("Found: {!s}".format(self.local_path))

    def getlocalfolder(self):
        """
        acces private variable of local path and return string
        :rtype: basestring
        """
        return self.local_path

    def upgrade(self, inputfile):
        """
        Args:
           :inputzipfile (str): content reference path to extract
         """  # load the zip file in read mode
        archive = zip.ZipFile(inputfile, 'r')
        archive.extractall(self.__PATH)
        archive.close()

    def cleanup(self, inputfile):
        print('ok')
        try:
            os.remove(inputfile)
        except OSError as e:  # if failed, report it back to the user
            print("Error: %s - %s." % (e.filename, e.strerror))

    # message = PrintColour("Delete").setcolour('lightyellow') + "{!s}".format(inputfile) + "file"
    # print(message, sep='\n')


if __name__ == '__main__':
    outzip = '/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/elvui-10.78.zip'

    test = Filemanager()
    test.upgrade()  # outzip)
    test.cleanup(outzip)
