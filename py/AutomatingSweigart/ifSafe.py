"""Program checking if password is safe using regex.
"""
import re

def ifSafe(password):
    ifDigit = re.compile('\d+')
    ifLowerCase = re.compile('[a-z]+')
    ifUpperCase = re.compile('[A-Z]+')
    ifLongEnough = re.compile('.{8,}')
    ifSpecialChar = re.compile('[!"#$%&()\*\+,\\-\./:;<=>?@[\]^_`{|}~]+')

    if not ifDigit.search(password):
        return 'Your password must contain at least one digit.'
    elif not ifLowerCase.search(password):
        return 'Your password must contain at least 1 lowercase.'
    elif not ifUpperCase.search(password):
        return 'Your password must contain at least 1 uppercase.'
    elif not ifLongEnough.search(password):
        return 'Your password must be at least 8 characters long.'
    elif not ifSpecialChar.search(password):
        return 'Your password must contain at least 1 special character.'
    else:
        return 'This password is safe.'


print(ifSafe('8uBru%jie'))