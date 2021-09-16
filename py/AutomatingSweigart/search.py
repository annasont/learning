'''Program that opens all .txt files in a given directory and searches for any
line that matches a user-supplied regular expression.
'''
import os, re

print('Enter regular expression, you want to search for:')
regex = input()

print('Enter a path to the folder with files to check:')
path = input()

searchfor = re.compile(regex, re.I)

for filename in os.listdir(path):
    if filename.endswith('.txt'):
        checkfile = open('%s/%s' % (path, filename))
        res = searchfor.findall(checkfile.read())
        print('\n%s:' % filename)
        for result in res:
            print(result)
