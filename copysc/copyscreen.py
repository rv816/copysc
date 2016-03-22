#! /usr/bin/env python

import mechanicalsoup as ms
from itertools import islice
import re
import pyperclip
import sys
import warnings

def convert_clipboard(link = None):
    browse = ms.Browser()
    if not link:
        link = pyperclip.paste()

    if 'dropbox' in link:
        link2 = re.sub('\?.+$', '', link)
        newlink = str(link2) + '?raw=1'
        pyperclip.copy(newlink)
        return newlink

    else:
        pg = browse.get(link)
        string = pg.soup.findAll('img')
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
            try:
                convert_clipboard(link)
            except Warning:
                convert_clipboard(link)
    except Exception as err:
        print(err)
        print('Either pass an argument or try again with a different link.')
