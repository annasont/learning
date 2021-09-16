'''backupToZip.py is craating back up zip file with all files in current working directory.
New back up-files will be given new ordinal number.  
'''

import zipfile, os, re

#my version

# cwd = os.getcwd()
# listOfFiles = os.listdir(cwd)
# separator = ' '
# strigWithFilenames = separator.join(listOfFiles)
# number = re.compile('backup_(\d).zip')

# foundZip = number.findall(strigWithFilenames)
# if foundZip:
#     n = len(foundZip)
# else:
#     n = 0

# backup = zipfile.ZipFile('backup_%d.zip' % (n + 1), 'w')
# for item in listOfFiles:
#     if not item.startswith('backup'):
#         backup.write(item, compress_type=zipfile.ZIP_DEFLATED)
# backup.close()


def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = '%s_%s.zip' % (os.path.basename(folder), str(number))
        if not os.path.exists(zipFilename): 
            break
        number += 1
    print('Creating %s...' % zipFilename)
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s to zip.' % foldername)
        backupZip.write(foldername, compress_type=zipfile.ZIP_DEFLATED)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename), compress_type=zipfile.ZIP_DEFLATED)

print(backupToZip('.'))

