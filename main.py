# !/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import urllib.error
import urllib.parse
import urllib.request

import requests
from tqdm import tqdm


class Addondownloader:
    """Addondownloader class manage the information about AddOn version:
        - verify in local pc and return installed version
        - verify remote AddOn version from https://www.tukui.org/download.php?ui=elvui
        - download the file from https://www.tukui.org/downloads/elvui-x.x.zip
    Input parameter:
    localpath as Local folder where are stored the AddOn in general ~/Applications/World of Warcraft/Interface/AddOns
    Return parameters
       addonversion as Local Add-On version
       remoteversion as Remote Add-On version
    """
    # initialize parameters:
    # interface version
    interfaceversion = 0

    # local Add-On version
    addonversion = 0

    # remote Add-On version
    remoteversion = 0

    def __init__(self):
        super().__init__()

    def checklocalversion(self, localpath):
        """Checklocalverison retrive information from local 'file'.toc and save the value Interface's version and the value
        AddOn's version """
        print("Checking Add-On version")

        # open file and read information
        with open(localpath + "ElvUI.toc", "r") as f:
            stream = f.read().split('\n')
            for line in stream:
                if "Interface" in line:
                    self.interfaceversion = self.version(line)

                if "Version" in line:
                    self.addonversion = self.version(line)

        print("Local ElvUI Add-On version: {!s}".format(self.addonversion))

    @staticmethod
    def version(line):
        """getversion used to extract by regex information about number version fo any field"""

        # set pattern to extract information
        versionsearched = re.search(r"(?P<version>\d+.\d+)", line)
        if versionsearched:
            version = versionsearched.group('version')
            return version

    def checkremoteversion(self):
        """Checkremoteverison retrive information from remote site 'https://www.tukui.org/download.php?ui=elvui'
        the actual version of the Add-On"""

        # store locally webpage Add-On
        url = 'https://www.tukui.org/download.php?ui=elvui'
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            stream = response.read()

        # covert remote source page to string
        sourcepage = str(stream)

        # extract version
        remotesearch = re.search(
            r"<a href=\"/downloads/elvui-(?P<version>\d+.\d+).zip\" class=\"btn btn-mod btn-border-w btn-round btn-large\">",
            sourcepage)
        if remotesearch:
            self.remoteversion = remotesearch.group('version')
            print("Remote ElvUI Add-On version: {!s}".format(self.remoteversion))
            return self.remoteversion

    def update(self):
        """updade start the donwload of the file"""
        # set original link
        originalurl = "https://www.tukui.org/downloads/elvui-0.0.zip"
        downloadurl = re.sub("(?P<version>\d+.\d+)", self.remoteversion, originalurl)

        # download new version
        orginalsavefile = "elvui-0.0.zip"
        savefile = re.sub("(?P<version>\d+.\d+)", self.remoteversion, orginalsavefile)

        # launch progress bar and download new version
        r = requests.get(downloadurl, stream=True)
        total_size = int(r.headers["Content-Length"])
        downloaded = 0  # keep track of size downloaded so far
        chunksize = 1024
        bars = int(total_size / chunksize)
        with open(savefile, "wb") as f:
            for chunk in tqdm(r.iter_content(chunk_size=chunksize), total=bars, unit="kB",
                              desc=savefile, leave=True, dynamic_ncols=True):
                f.write(chunk)
                downloaded += chunksize  # increment the downloaded

        print("Download complete")
        return savefile

    def getlocalversion(self):
        return float(self.addonversion)

    def getremoteversion(self):
        return float(self.remoteversion)


class Maketitle:
    name = "Francesco"
    surname = "Argentieri"
    License = "MIT"

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
              "\t\tAuthor: {!s}".format(self.name + " " + self.surname),
              "\n\tLicense: {!s}".format(self.License), end='\n')


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