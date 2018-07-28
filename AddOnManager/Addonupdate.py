# !/usr/bin/python3
# -*- coding: utf-8 -*-


import re
import urllib.error
import urllib.parse
import urllib.request

import requests
from tqdm import tqdm

from .colour import PrintColour


class Addonupdate:
    """Addonupdate class manage the information about AddOn version:
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

    def checklocalversion(self, p_path):
        """Checklocalverison retrive information from local 'file'.toc and save the value Interface's version and the
        value AddOn's version """
        print("Checking Add-On version")

        # open file and read information
        with open(p_path, "r") as f:
            stream = f.read().split('\n')
            for line in stream:
                if "Interface" in line:
                    self.interfaceversion = self.__version(line)

                if "Version" in line:
                    self.addonversion = self.__version(line)

        result = PrintColour(self.addonversion).setcolour('blue')
        print("Local ElvUI Add-On version: {!s}".format(result))

    def __version(self, line):
        """
        getversion used to extract by regex information about number version from field of table of content (.toc)
        Args:
            line (str):  line extract content information
        :returns:  int -- version find out.
        """
        # set pattern to extract information
        versionsearched = re.search(r"(?P<version>\d+.\d+)", line)
        if versionsearched:
            version = versionsearched.group('version')
            return version

    def checkremoteversion(self):
        """Checkremoteverison retrive information from remote site 'https://www.tukui.org/download.php?ui=elvui'
        the actual version of the Add-On
        :returns:  int -- remote version the add-on.
        """

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
            print("Remote version: {!s}".format(PrintColour(self.remoteversion).setcolour('green')))
        else:
            print(PrintColour("Remote version not avaiable.").setcolour('red'))

        return self.remoteversion

    def update(self):
        """
        check the remote version at link hard coded
        :return: string -- path of the file zip
        """
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
            for chunk in tqdm(r.iter_content(chunk_size=chunksize), total=bars, unit="kB", ncols=80,
                              desc=savefile, leave=True):
                f.write(chunk)
                downloaded += chunksize  # increment the downloaded

        PrintColour("Download complete").setcolour('green')
        return savefile

    def getlocalversion(self):
        return float(self.addonversion)

    def getremoteversion(self):
        return float(self.remoteversion)

