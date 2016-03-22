Convert "Screenshot-sharing" utility links to markdown-ready \*.png files I'm sure you are also annoyed that screenshot-sharing utilities like Screencloud and Dropbox only copy a link to their screenshot viewing page, not to the ``.png`` file itself.
==========================================================================================================================================================================================================================================================

So, if you have a python window open, use this module to quickly
``convert_clipboard()`` to a downloadable link.

In the backgound, this simply accesses the page linked by the
screenshot-sharing utility using ``mechanicalsoup``, finds the first
link that ends in png using regex, and copies that to the clipboard
using pyperclip.

Installation
------------

Python Module
^^^^^^^^^^^^^

``pip install copysc``

or

.. code:: bash

    $ git clone https://github.com/rv816/copysc.git
    $ cd copysc
    $ python setup.py install

Command Line Utility
^^^^^^^^^^^^^^^^^^^^

*Linux*
'''''''

``$ echo export PATH=$PATH:$(python -c 'import copysc; print(copysc.__path__[0])') >> ~/.bashrc``

You may also need to install a clipboard drivers to enable pyperclip to
interact with your X clipboard.

::

    $ sudo apt-get install xclip
    $ sudo apt-get install xsel

*Mac*
'''''

``$ echo export PATH=$PATH:$(python -c 'import copysc; print(copysc.__path__[0])') >> ~/.bash_profile``

*Windows*
'''''''''

Install Linux or buy a Mac and see above.

*I'm sorry. That was a bit rude. I'm sure it's possible, but I don't
have the faintest idea how Windows works* *My hunch is as follows:*

1. Find out the absolute path of the module as follows:
   ``C:\>python -c 'import copysc; print(copysc.__path__[0])'``

2. Copy that path and add it to your PATH variable on windows.

--------------

Usage:
------

As python module:
~~~~~~~~~~~~~~~~~

.. code:: python

    from copysc.copyscreen import convert_clipboard
    convert_clipboard()

OR...you can feed it a link directly

.. code:: python

    from copysc.copyscreen import convert_clipboard
    convert_clipboard(link= 'https://www.dropbox.com/s/wg24eyirfaqrbnw/Screenshot%202014-10-17%2018.06.22.png?dl=0')

From the command line:
~~~~~~~~~~~~~~~~~~~~~~

``$ copyscreen https://www.dropbox.com/s/wg24eyirfaqrbnw/Screenshot%202014-10-17%2018.06.22.png?dl=0``

OR to directly access the clipboard

``$ copyscreen``
