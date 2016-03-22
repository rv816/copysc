#Convert "Screenshot-sharing" utility links to markdown-ready *.png files
I'm sure you are also annoyed that screenshot-sharing utilities like Screencloud and Dropbox only copy a link to their screenshot viewing page, not to the `.png` file itself. 


So, if you have a python window open, use this module to quickly `convert_clipboard()` to a downloadable link.

In the backgound, this simply accesses the page linked by the screenshot-sharing utility using `requests`, parses it with BeautifulSoup,  finds the first link that ends in png using regex, and copies that to the clipboard using pyperclip. 

## Installation

#### Python Module 

`pip install copysc`

or
```bash
$ git clone https://github.com/rv816/copysc.git
$ cd copysc
$ python setup.py install
```

#### Command Line Utility
##### _Linux_

```bash
$ export copyscpath=$(python -c 'import copysc; print(copysc.__path__[0])')
$ echo export PATH=$PATH:$copyscpath >> ~/.bashrc
$ sudo chmod 755 $copyscpath/copyscreen.py
```

You may also need to install a clipboard drivers to enable pyperclip to interact with your X clipboard.

```
$ sudo apt-get install xclip
$ sudo apt-get install xsel
```


##### _Mac_

```bash
$ export copyscpath=$(python -c 'import copysc; print(copysc.__path__[0])')
$ echo export PATH=$PATH:$copyscpath >> ~/.bash_profile
$ sudo chmod 755 $copyscpath/copyscreen.py
```

##### _Windows_

Install Linux or buy a Mac and see above.

_I'm sorry. That was a bit rude. I'm sure it's possible, but I don't have the faintest idea how Windows works_
_My hunch is as follows:_

1. Find out the absolute path of the module as follows:
`C:\>python -c 'import copysc; print(copysc.__path__[0])'`

2. Copy that path and add it to your PATH variable on windows.

______ 

## Usage:

### As python module:

```python
from copysc.copyscreen import convert_clipboard
convert_clipboard()

```

OR...you can feed it a link directly
```python
from copysc.copyscreen import convert_clipboard
convert_clipboard(link= 'https://www.dropbox.com/s/wg24eyirfaqrbnw/Screenshot%202014-10-17%2018.06.22.png?dl=0')

```

### From the command line:

`$ copyscreen`

_or_


`$ copyscreen http://screencloud.net/v/zOk6`




