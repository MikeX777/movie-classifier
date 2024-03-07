import zipfile
import time
import sys
import shutil
import re
import os
import logging
import json
import hashlib
import glob

import click
import requests
from bs4 import BeautifulSoup
import urllib.request

# List of ISO 639-1 two-letter language codes
# (reference: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)
# This list is *very* incomplete. If your language doesn't appear here,
# feel free to add to the list. The program should still function as expected.
LANGUAGE_CODES = {
    "English": "en",
}

def get_from_subdb(directory, movie_name, language, verbose=False):
    try:
        form_data = { "q": movie_name }
        r = requests.post("https://subscene.com/subtitles/release", files=form_data)
        soup=BeautifulSoup(r.content,"lxml")
        atags=soup.find_all("a")
        href=""
        print(soup)
        for i in range(0,len(atags)):
            spans=atags[i].find_all("span")
            if(len(spans)==2 and spans[0].get_text().strip()==language and spans[1].get_text().strip()==movie_name):
                href=atags[i].get("href").strip()
        print(href)

        if (len(href)>0):
            r=requests.get("http://subscene.com"+href);
            soup=BeautifulSoup(r.content,"lxml")
            lin=soup.find_all('a',attrs={'id':'downloadButton'})[0].get("href")
            print('this lint', lin)
            r=requests.get("http://subscene.com"+lin);
            soup=BeautifulSoup(r.content,"lxml")
            subfile=open(directory +" {}.zip".format(language), 'wb')
            for chunk in r.iter_content(100000):
                subfile.write(chunk)
                subfile.close()
                time.sleep(1)
                zip_=zipfile.ZipFile(directory +" {}.zip".format(language)) #Naming zip is not recommended renamed it to zip_ (Following PEP 8 convention)
                zip_.extractall(directory)                                 #Naming it as zip would overwrite built-in function zip
                zip_.close()
                os.unlink(directory +" {}.zip".format(language))
                shutil.move(directory +zip.namelist()[0], os.path.join(directory, movie_name + " {}.srt".format(language)))
    except:
        #Ignore exception and continue
        print("Error in fetching subtitle for " + movie_name)
        print("Error", sys.exc_info())
        logging.error("Error in fetching subtitle for " + movie_name + str(sys.exc_info()))

test = get_from_subdb("./data_retrieval/subtitle_retrieval/", "joker", "en", True)
print(test)