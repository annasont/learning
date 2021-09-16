'''fillInGaps.py finds files with given prefix, locates gaps in numbering. 
NB: files have to have same number of digits in their names.
'''

import os, re, shutil

def findAndSortFilenames(prefix, folder):
    #function find files with given prefix and search in given folder
    #first argument - prefix without extension of the file
    #second argument - path to the folder we want to sarch through 
    abspath = os.path.abspath(folder)
    listfiles = os.listdir(abspath)
    findFile = re.compile(prefix + '(\d+)' + '(.+)')
    allNumbers = []
    for filename in listfiles:
        if filename.startswith(prefix):
            res = findFile.search(filename)
            number = res.group(1)
            extension = res.group(2)
            allNumbers.append(number)
    allNumbersSorted = sorted(allNumbers)
    return extension, allNumbersSorted

def fillInGaps(prefix, folder):
    #function renames files (eg. text001.txt, text003.txt renames to text001.txt, text002.txt)
    extension, allNumbersSorted = findAndSortFilenames(prefix, folder)

    indeks = 1
    for number in allNumbersSorted:
        if int(number) == indeks:
            indeks +=1
        else:
            path = os.path.join(folder, (prefix + number + extension))
            zeros = '0' * (len(number) - len(str(indeks)))
            pathRenamed = os.path.join(folder, (prefix + zeros + str(indeks) + extension))
            shutil.move(path, pathRenamed)
            print('Changing filename %s to %s' % ((prefix + number + extension), (prefix + zeros + str(indeks) + extension)))
            indeks += 1


def locateGaps(prefix, folder, indeks=1):
    #function finds gaps in numbering and creates new empty files
    extension, allNumbersSorted = findAndSortFilenames(prefix, folder)

    regLastnumber = re.compile('0*(\d+)')
    res = regLastnumber.search(allNumbersSorted[-1])
    lastNumber = (res.group(1))
    
    allNumbersInt = []
    for i in range(len(allNumbersSorted)):
        allNumbersInt.append(int(allNumbersSorted[i]))

    missingNumbers = []
    for i in range(1, int(lastNumber)):
        if not i in allNumbersInt:
            missingNumbers.append(i)

    for i in missingNumbers:
        strI = str(i)
        if len(allNumbersSorted[0]) == len(str(i)):
            zeros = ''
        else: 
            zeros = '0' * (len(allNumbersSorted[0]) - len(str(i)))
        filenameNew = prefix + zeros + str(i) + extension
        open(os.path.join(folder, filenameNew), 'w')
        print('File %s created.' % filenameNew)


#print(locateGaps('text', './f'))