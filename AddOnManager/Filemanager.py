# !/usr/bin/python3
# -*- coding: utf-8 -*-
import platform
import os
import sys

import time
import zipfile
import shutil
from tqdm import tqdm
from send2trash import send2trash


class Filemanager:
    __tempname = 'TempFolderAddon'
    __zipfile = ''

    def __init__(self, inputfile):
        self.__zipfile = inputfile

    def maketempfolder(self):
        # load the zip file in read mode
        archive = zipfile.ZipFile(self.__zipfile, 'r')

        # prints the content
        print(archive.printdir())

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

    def copytree(src, dst, symlinks=False):
        names = os.listdir(src)
        os.makedirs(dst)
        errors = []
        for name in names:
            srcname = os.path.join(src, name)
            dstname = os.path.join(dst, name)

    def coopy(self,
              src='/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/AddOnManager/TempFolderAddon/',
              dst='/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/2/', symlinks=False):

        names = os.listdir(src)
        print(names)
        # os.makedirs(dst)
        errors = []
        srcname = []
        for name in names:
            srcname = os.path.join(src, name)
            print(srcname, end='\n')
            dstname = os.path.join(dst, name)
            # print(dstname, end='\n')

            # print(type(bar))
            # self.copyDirectoryTree(bar, dstname)
            bar = tqdm()



            # def copy(source, destination, filetype):
            #     source = source + '\\' + filetype
            #     destination = destination + '\\' + filetype
            #     bar = tqdm(os.listdir(source))
            #     for directory in bar:
            #         try: shutil.copytree(source + '\\' + directory, destination + '\\' + directory + ' Copied')
            #         print except: continue
            #
            # for folder in name:
            #   print(folder)
            # bar = tqdm(folder)
            # for x in bar:
            #    print(x)
            # self.copyDirectoryTree(bar, dstname)

    def copyDirectoryTree(self, root_src_dir, root_dst_dir):
        """
        Copy directory tree. Overwrites also read only files.
        :param root_src_dir: source directory
        :param root_dst_dir:  destination directory
        """

        for src_dir, dirs, files in os.walk(root_src_dir):
            dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)

        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                try:
                    os.remove(dst_file)
                except PermissionError as exc:
                    os.chmod(dst_file, stat.S_IWUSR)
                    os.remove(dst_file)

            shutil.copy(src_file, dst_dir)


# src = '/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/tmp'
# dst = '/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/2'
# def copy():
#     #shutil.copytree(src, dst)
#     if os.path.exists(dst):
#         print('Folder exist, then all file overwrite\n\tPorced: yes or no?')
#         shutil.rmtree(dst)
#     shutil.copytree(src, dst)
#
#
#
#
# def process_content_with_progress3(inputpath = src, blocksize=1024):
#     # Preprocess the total files sizes
#     sizecounter = 0
#     for filepath in tqdm(os.listdir(inputpath), unit="files"):
#         print(os.walk(inputpath))
#         sizecounter += os.stat(filepath).st_size
#
#     # Load tqdm with size counter instead of file counter
#     with tqdm(total=sizecounter,
#               unit='B', unit_scale=True, unit_divisor=1024) as pbar:
#         for filepath in walkdir(inputpath):
#             with open(filepath, 'rb') as fh:
#                 buf = 1
#                 while (buf):
#                     buf = fh.read(blocksize)
#                     dosomething(buf)
#                     if buf:
#                         pbar.set_postfix(file=filepath[-10:], refresh=False)
#                         pbar.update(len(buf))


if __name__ == '__main__':
    outzip = '/Users/francescoargentieri/PycharmProjects/ElvUIAddOnManager/elvui-10.68.zip'

    # process_content_with_progress3()

    test = Filemanager(outzip)
    test.maketempfolder()
    # test.coopy()

    #
    # def copy(source, destination, filetype):
    #     source = source + '\\' + filetype
    #     destination = destination + '\\' + filetype
    #     bar = tqdm(os.listdir(source))
    #     for directory in bar:
    #         try: shutil.copytree(source + '\\' + directory, destination + '\\' + directory + ' Copied')
    #         print except: continue
    #
    #
    # copy()
