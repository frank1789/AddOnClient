# !/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, time
import os
import re
import zipfile
import shutil
from tqdm import tqdm
from send2trash import send2trash


class Filemanager:
    __tempname = 'TempFolderAddon'
    __zipfile = ''
    # initialize list of file to copy
    __path = []

    def __init__(self, inputfile):
        # load the file
        self.__zipfile = inputfile
        self.maketempfolder()

    def maketempfolder(self):
        # load the zip file in read mode
        archive = zipfile.ZipFile(self.__zipfile, 'r')
        # prints the content
        # print(archive.printdir())  # enable for debug
        # make a temporary directory
        try:
            os.makedirs('TempFolderAddon')
            print('Created temporary folder: ', self.__tempname)

        except OSError:
            if os.path.exists(self.__tempname):
                print('Folder already exist')
                #  move to trash
                send2trash(self.__tempname)

        archive.extractall(self.__tempname)

    def __deletetempfolder(self):
        if os.path.exists(self.__tempname):
            #  move to trash
            send2trash(self.__tempname)
            print('Delete temporary files\n')

    def __deletezipfile(self):
        if os.path.exists(self.__zipfile):
            #  move to trash
            send2trash(self.__zipfile)
            print('Delete zip files\n')

    def upgrade(self):
        # search file in target folder
        for root, dirs, files in os.walk("."):
            for file in files:
                # make string of path
                tmp = root + '/' + file
                if '/TempFolderAddon/' in tmp:
                    # print(tmp) # enable for debug
                    self.__path.append(root + '/' + file)
                else:
                    pass

        # launch copy of file
        # notify(title='ElvUI Add-On Manager', subtitle='with python', message='Start copy of files...')
        with tqdm(range(len(self.__path)), desc='start') as pbar:
            for i in range(len(self.__path)):
                # time.sleep(0.01)
                self.destinationfile(self.__path[i])
                pbar.update()
                pbar.set_description('copy {}'.format(self.__extractnameextfile(self.__path[i])))
                # print(self.__extractnameextfile(self.__path[i]), self.destinationfile(self.__path[i]),end='\n')
                # copy function file to file
                shutil.copyfile(self.__path[i], self.destinationfile(self.__path[i]))
                pass

                # print("Copy complete")

    def __extractnameextfile(self, filepath):
        searched = re.search(r"(.+\/)(?P<fieldnames>[^\/]+)$", filepath)
        file_name_ext = searched.group('fieldnames')
        # print(searched.group('fieldnames')) # enable for debug
        return file_name_ext

    def destinationfile(self, sourcepathfile):

        destination = re.sub(r'(\.\/\w+\/)', '/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/2/',
                             sourcepathfile)
        # print(sourcepathfile,  destination, sep=' ', end='\n') # enable for debug
        return destination

        # def __del__(self):
        # self.__deletezipfile()
        # self.__deletetempfolder()


if __name__ == '__main__':
    outzip = '/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/elvui-10.68.zip'
    src = '/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/AddOnManager/TempFolderAddon/'
    dst = '/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/2/'

    test = Filemanager(outzip)
    test.upgrade()