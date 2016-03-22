#! /usr/bin/env python

import bs4
from itertools import islice
import re
import pyperclip
import sys
import warnings
import requests


def convert_clipboard(link = None):
    if not link:
        link = pyperclip.paste()

    if 'dropbox' in link:
        link2 = re.sub('\?.+$', '', link)
        newlink = str(link2) + '?raw=1'
        pyperclip.copy(newlink)
        return newlink

    else:
        pg = requests.get(link)
        string_pre = bs4.BeautifulSoup(pg.content, "html.parser")
        string = string_pre.findAll('img')
        filted = filter(lambda x: re.findall('//.+png', x.attrs.get('src')), string)
        for x in filted:
            tocopy = str('http://' + str(re.findall('//.+png', x.attrs['src'])[0].strip('//')))
            pyperclip.copy(tocopy)
            print(tocopy + " copied to clipboard")
            return tocopy

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            link = sys.argv[1]
        else:
            link = None

        convert_clipboard(link)
    except Exception as err:
        print(err)
        print('Either pass an argument or try again with a different link.')
