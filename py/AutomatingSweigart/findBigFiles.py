'''Find big files or folders in given location.
'''
import os

def findBigFiles(path, biggerThan):
    #function that finds big files
    #argument path: path to location you want to serach through
    #biggerThan: size in MB - function will find all files that are equal or bigger
    path = os.path.abspath(path)
    biggerThanMB = biggerThan * 1000000
    found = False
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            abspath = os.path.join(foldername, filename)
            size = os.path.getsize(abspath)
            if size >= biggerThanMB:
                print('Filename: %s, size: %s MB\npath: %s' % (filename, round(size / 1000000, 2), abspath))
                found = True
    if found == False:
        print('No files bigger than %s MB' % biggerThan)
    
    
            

def findBigFolders(path, biggerThan, name=''):
    #function that finds big folders
    #argument path: absoluth path to location you want to serach through
    #biggerThan: size in MB - function will find all folders that are equal or bigger
    path = os.path.abspath(path)
    biggerThanMB = biggerThan * 1000000
    totalSize = 0
    for f in os.listdir(path):
        fp = os.path.join(path, f)
        if os.path.isfile(fp):
            totalSize += os.path.getsize(fp)
        else:
            findBigFolders(fp, biggerThan, f)
    
    if totalSize >= biggerThanMB:
        print('Folder: %s, totalSize: %s MB\npath: %s' % (name, round(totalSize / 1000000, 2), os.path.join(path)))
    

if __name__ == '__main__':
    # print('Insert path to location you want to search thorugh:')
    # x = input()
    # print('I want to find files that are equal or bigger than (MB):')
    # y = float(input())
    # print(findBigFiles(x, y))
    print('\nInsert path to location you want to search thorugh:')
    x = input()
    print('I want to find folders that are equal or bigger than (MB):')
    y = float(input())
    print(findBigFolders(x, y))
    