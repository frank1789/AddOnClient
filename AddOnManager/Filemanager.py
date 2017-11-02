# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import re
import zipfile
import shutil
from tqdm import tqdm
from send2trash import send2trash
from notifyme import notify


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
        notify(title='ElvUI Add-On Manager', subtitle='with python', message='Start copy of files...')
        with tqdm(range(len(self.__path)), desc='start') as pbar:
            for i in range(len(self.__path)):
                pbar.set_description('copy file {:<35}'.format(self.__extractnameextfile(self.__path[i])))
                # todo insert function of copy
                pbar.update()
                pass

    def __extractnameextfile(self, filepath):
        searched = re.search(r"(.+\/)(?P<fieldnames>[^\/]+)$", filepath)
        file_name_ext = searched.group('fieldnames')
        # print(searched.group('namewithext')) # enable for debug
        return file_name_ext


if __name__ == '__main__':
    outzip = '/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/elvui-10.68.zip'
    src = '/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/AddOnManager/TempFolderAddon/'
    dst = '/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/2/'

    test = Filemanager(outzip)
    test.upgrade()

    # try:
    #     shutil.copytree(src, dst)
    #     # Directories are the same
    # except shutil.Error as e:
    #     print('Directory not copied. Error: %s' % e)
    #     # Any error saying that the directory doesn't exist
    # except OSError as e:
    #     print('Directory not copied. Error: %s' % e)
    # #finally:
    #  #
    #   #  print('Over')
    #
    # for item in os.listdir(src):
    #     print(item)
    #
    #
    # for item in os.listdir(src):
    #     srcFile = os.path.join(src, item)
    #     dstFile = os.path.join(dst, item)
    #     print(srcFile)
    #     shutil.copy2(srcFile, dstFile)




    # process_content_with_progress3()

    # test = Filemanager(outzip)
    # test.maketempfolder()
    # test.test(src, dst)


    # shutil.copy2(pa[i], '/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/2/ElvUI/')
    # print((len(path) - 1) * '---', os.path.basename(root))
    # print(root)
    # pa.append(root)






    # for file in files:
    # print(len(path) * '---', file)
    #    print(file)
    # a = os.listdir(src)
    # print(os.walk('.'))
    # print(os.listdir(src))
    # print(type(a))

    # bar = tqdm(files)
    # print(bar)
    # for file in root:
    #    print(file)
    #    shutil.copytree(file,'/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/2')
    # print(pa)
    # for i in pa:
    #     os.listdir(i)
    # bar = tqdm(dirs)
    # for directory in bar:
    # print(directory)
    #    shutil.copyfile(directory, dst)
    #
    # def copy(source, destination, filetype):
    #     source = source + '\\' + filetype
    #     destination = destination + '\\' + filetype
    #     bar = tqdm(os.listdir(source))
    #     for directory in bar:
    #         try: shutil.copytree(source + '\\' + directory, destination + '\\' + directory + ' Copied')
    #         print except: continue
