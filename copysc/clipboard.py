#! /usr/bin/env python

import mechanicalsoup as ms
from itertools import islice
import re
import pyperclip


def convert_clipboard(link = None):
    browse = ms.Browser()
    if not link:
        link = pyperclip.paste()
        
    if 'dropbox' in link:
        link = link.strip('?dl=0')
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
    convert_clipboard()
