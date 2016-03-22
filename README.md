# Convert "Screenshot-sharing" utility links to markdown-ready *.png files
I'm sure you are also annoyed that screenshot-sharing utilities like Screencloud and Dropbox only copy a link to their screenshot viewing page, not to the `.png` file itself. 


So, if you have a python window open, use this module to quickly `convert_clipboard()` to a downloadable link.

In the backgound, this simply accesses the page linked by the screenshot-sharing utility using `mechanicalsoup`, finds the first link that ends in png using regex, and copies that to the clipboard using pyperclip. 


Usage:

```python
from copysc.clipboard import convert_clipboard
convert_clipboard()

```

OR...you can feed it a link directly
```python
from copysc.clipboard import convert_clipboard
convert_clipboard(link=)

```

