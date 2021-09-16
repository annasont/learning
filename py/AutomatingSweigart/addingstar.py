'''Program that adds star and space before every sentence'''

import sys, pyperclip


pyperclip.copy('jakis tam tekst, \nktóry jest w kilku liniach \ni nic więcej')
text = pyperclip.paste()

if text:
    lines = text.split('\n')
    formattedText = ''
    for line in lines:
        formattedText += '* %s\n' % line
    pyperclip.copy(formattedText)
    print('Text formatted succesfully. Ready to paste!')
else:
    print('Copy some text to clipboard')