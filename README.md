# Convert "Screenshot-sharing" utility links to markdown-ready *.png files
I'm sure you are also annoyed that screenshot-sharing utilities like Screencloud and Dropbox only copy a link to their screenshot viewing page, not to the `.png` file itself.


If you've installed as a command line utility, simply type `copyscreen` at the command prompt to fetch the actual image file from the link that is currently in your clipboard (or, alternatively, pass the link directly as an argument (`copyscreen http://dropbox.screenshotaddress.com?dl=0`).

 If you are using python, use this module to quickly `convert_clipboard()` to a downloadable link.

In the background, this simply accesses the page linked by the screenshot-sharing utility using `requests`, parses it with `BeautifulSoup`,  finds the first link that ends in png using regex, and copies that to the clipboard using `pyperclip`.

## Installation

#### Python Module

```pip install copysc```

or
```bash
$ git clone https://github.com/rv816/copysc.git
$ cd copysc
$ python setup.py install
```

#### Command Line Utility


##### _Mac_

```bash
$ export copyscpath=$(python -c 'import copysc; print(copysc.__path__[0])')
$ sudo chmod 755 $copyscpath/copyscreen.py
$ ln -s $copyscpath/copyscreen.py $copyscpath/copyscreen
$ echo export PATH=$PATH:$copyscpath >> ~/.bash_profile
```
Note: If symlink already exists (at step 3: ln -s ....), then just move on to next step. I've tried to configure the installer to install the symlink, but that's still in alpha and may not work.

##### _Linux_

```bash
$ export copyscpath=$(python -c 'import copysc; print(copysc.__path__[0])')
$ sudo chmod 755 $copyscpath/copyscreen.py
$ ln -s $copyscpath/copyscreen.py $copyscpath/copyscreen
$ echo export PATH=$PATH:$copyscpath >> ~/.bashrc
```
Note: If symlink already exists (at step 3: ln -s ....), then just move on to next step. I've tried to configure the installer to install the symlink, but that's still in alpha and may not work.

You may also need to install a clipboard drivers to enable pyperclip to interact with your X clipboard.

```
$ sudo apt-get install xclip
$ sudo apt-get install xsel
```



##### _Windows_

Install Linux or buy a Mac and see above.

_I kid.  I'm sure it's possible, but I don't have the faintest idea how Windows works_
_My hunch is that the below instructions might be helpful:_

1. Find out the absolute path of the module as follows:
`C:\>python -c 'import copysc; print(copysc.__path__[0])'`

2. Copy the output of **Step 1** to the clipboard.
3. Add the path you copied above to your PATH variable on windows as follows:
> From the desktop, right click the My Computer icon.
> 1. Choose Properties from the context menu.
> 2. Click the Advanced tab (Advanced system settings link in Vista).
> 3. Click Environment Variables. You should see something that looks like this: ![environ](http://www.computerhope.com/issues/pictures/winpath.jpg) 
> 4. Select "Path" and click "Edit".
> 5. In Windows 10, you should see something like this: ![win10](http://www.howtogeek.com/wp-content/uploads/2016/03/527x501x2016-03-24_11h02_18.png.pagespeed.gp+jp+jw+pj+js+rj+rp+rw+ri+cp+md.ic.tCgwD5Bcex.png). 
> 6. Click "New" and add the directory you copied above
> -  **IMPORTANT**: If you have Windows XP, 7, or 8, you will need to edit the text of `PATH` diretly. Instead of Step 5 above, you will need to add a semicolon (";") at the end of the value currently assigned to the `PATH` variable, and **then** paste teh value you copied above in Step 2.
> 7. Save the results and go back to the "Envornmnetal Variables" window you saw in **Step 3**. 
> 8. Select "PATHEXT" and click "Edit". (Note: if it's not there, create it as a new system variable.)
> 9. Click "New" and add ".py" (without the quotes). This tells windows to treat files ending in ".py" as an executible, so you can simply type "copyscreen" from the command line. If you do not want to do this (it is harmless), you will simply need to type copyscreen.py instead of copyscreen when using the utility.


Note:  PATH just has a list of directories to search when you type a command at the Command Prompt, so that if you type "copyscreen" at the command line, it will search the list of directories assigned to the PATH variable above. 


______

## Usage:

### From the command line:

`$ copyscreen`

_or_


`$ copyscreen http://screencloud.net/v/zOk6`

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
