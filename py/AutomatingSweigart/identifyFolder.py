'''Finding photo folders - folders that have more images than other files.'''
import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('/home/ania'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for subfolder in subfolders:
        for filename in filenames:
            formats = ['jpg', 'png', 'eps']
            if len(filename.split('.')) < 2:
                continue
            format = filename.split('.')[1]
            if format.lower() in formats:
                try:
                    image = Image.open(filename)
                    width, height = image.size
                    if width > 500 and height > 500:
                        numPhotoFiles += 1
                    else:
                        numNonPhotoFiles += 1
                except FileNotFoundError:
                    continue
            else:
                numNonPhotoFiles += 1

        if numPhotoFiles > numNonPhotoFiles:
            print('Folder %s is a photo folder' % os.path.abspath(subfolder))
        else:
            print('Folder %s is not a photo folder' % subfolder)
            
