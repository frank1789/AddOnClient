# !/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import re
import shutil
import zipfile
from send2trash import send2trash
from tqdm import tqdm


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

    def upgrade(self, inputzipfile):
        """
        Args:
           :inputzipfile (str): content reference path to extract
         """
        # load the zip file in read mode
        archive = zipfile.ZipFile(inputzipfile, 'r')
        # prints the content
        # print(archive.printdir())  # enable for debug
        # make a temporary directory
        # try:
        # os.makedirs('TempFolderAddon')
        #    print('Created temporary folder: ', self.__tempname)

        # except OSError:
        #    if os.path.exists(self.__tempname):
        # print('Folder already exist')
        #  move to trash
        #        send2trash(self.__tempname)

        archive.extractall(self.__PATH)


        # def __deletetempfolder(self):
        #     if os.path.exists(self.__tempname):
        #         #  move to trash
        #         send2trash(self.__tempname)
        #         print('Delete temporary files\n')
        #
        # def __deletezipfile(self):
        #     if os.path.exists(self.__zipfile):
        #         #  move to trash
        #         send2trash(self.__zipfile)
        #         print('Delete zip files\n')
        #
        # def upgrade(self):
        #     # search file in target folder
        #     for root, dirs, files in os.walk("."):
        #         for file in files:
        #             # make string of path
        #             tmp = root + '/' + file
        #             if '/TempFolderAddon/' in tmp:
        #                 # print(tmp) # enable for debug
        #                 self.__path.append(root + '/' + file)
        #             else:
        #                 pass
        #
        #     # launch copy of file
        #     # notify(title='ElvUI Add-On Manager', subtitle='with python', message='Start copy of files...')
        #     with tqdm(range(len(self.__path)), desc='start') as pbar:
        #         for i in range(len(self.__path)):
        #             # time.sleep(0.01)
        #             self.destinationfile(self.__path[i])
        #             pbar.update()
        #             pbar.set_description('copy {}'.format(self.__extractnameextfile(self.__path[i])))
        #             # print(self.__extractnameextfile(self.__path[i]), self.destinationfile(self.__path[i]),end='\n')
        #             # copy function file to file
        #             shutil.copyfile(self.__path[i], self.destinationfile(self.__path[i]))
        #             pass
        #
        #             # print("Copy complete")
        #
        # def __extractnameextfile(self, filepath):
        #     searched = re.search(r"(.+\/)(?P<fieldnames>[^\/]+)$", filepath)
        #     file_name_ext = searched.group('fieldnames')
        #     # print(searched.group('fieldnames')) # enable for debug
        #     return file_name_ext
        #
        # def destinationfile(self, sourcepathfile):
        #     destination = re.sub(r'(\.\/\w+\/)', '/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/2/',
        #                          sourcepathfile)
        #     # print(sourcepathfile,  destination, sep=' ', end='\n') # enable for debug
        #     return destination
        #
        #     # def __del__(self):
        #     # self.__deletezipfile()
        #     # self.__deletetempfolder()
        #
        # def newtest(self, dsrc, ddst):
        #     dsrc = self.maketempfolder(dsrc)
        #     # zip_filepath = '/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/elvui-10.68.zip'  # or glob.glob('...zip')
        #     # target_dir = 'test'
        #     #
        #     # for path in zip_filepath:
        #     #     with zipfile.ZipFile(path) as zf:
        #     #         dirname = os.path.join(
        #     #             target_dir, os.path.splitext(os.path.basename(path))[0]
        #     #         )
        #     #         zf.extract('A/B/C/target_file', path=dirname)
        #
        #     for dirname in os.listdir(dsrc):
        #         tocopy = os.path.join(dsrc, dirname)
        #         for d in os.listdir(tocopy):
        #             src = os.path.join(tocopy, d)
        #             dst = os.path.join(ddst, d)
        #             if os.path.isdir(src):
        #                 self.__copytree(src, dst)
        #
        # def __copytree(self, src, dst):
        #
        #     if os.path.isdir(src):
        #         if not os.path.exists(dst):
        #             os.makedirs(dst)
        #         for name in os.listdir(src):
        #             self.__copytree(os.path.join(src, name),
        #                      os.path.join(dst, name))
        #     else:
        #         shutil.copyfile(src, dst)


if __name__ == '__main__':
    outzip = '/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/elvui-10.68.zip'

    test = Filemanager()
    test.maketempfolder(outzip)
