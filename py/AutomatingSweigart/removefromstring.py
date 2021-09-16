"""Program remowing white spaces from beginning and end of string
    or removing what is passed in second argument in function.
"""
import re

def removeFromString(text, char=''):
    if not char:
        whiteCharFront = re.compile('^\s*')
        whiteCharBack = re.compile('\s*$')
        text = whiteCharFront.sub('', text)
        return whiteCharBack.sub('', text)
    else:
        reg = re.compile(char)
        return reg.sub('', text)

if __name__ == '__main__':
    mytext1 = 'Remowing vowels.'
    mytext2 = '   Remowing white characters.\n\n'
    print(mytext1)
    print(removeFromString(mytext1, char='[aeoui]'))
    print(mytext2)
    print(removeFromString(mytext2))