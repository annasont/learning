'''rename.py - Renames filenames in current working directory 
with American date format (MM-DD-YYYY)
to European date format (DD-MM-YYY)
'''
import re, os, shutil

cwd = os.getcwd()
filelist = os.listdir(cwd)

for filename in filelist:
    regexDate = re.compile('((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)')
    found = regexDate.search(filename)
    if found:
        month = found.group(1)
        day = found.group(3)
        year = found.group(5)
        dateEur = regexDate.sub('%s-%s-%s' % (day, month, year), filename)
        shutil.move(filename, dateEur)
