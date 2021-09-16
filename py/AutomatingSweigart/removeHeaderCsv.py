'''removeHeaderCsv.py remowes first line from all csv documents in given directory'''
import os, csv


def removeHeaderCsv(path):
    # Function takes path as an argument, removes first row in all csv files in given directory, and saves files in a new folder named headerRemoved 
    os.mkdir(os.path.join(path, 'headerRemoved'))
    csvFiles = []
    for filename in os.listdir(path):
        if filename.endswith('.csv'):
            csvFiles.append(filename)

    for filename in csvFiles:
        csvFile = open(filename)
        csvFileReader = csv.reader(csvFile)
        csvFileData = list(csvFileReader)
        csvFileData.pop(0)
        outputFile = open(os.path.join(path, 'headerRemoved', '%sCopy.csv' % filename[:-4]),'w', newline='')
        outputWriter = csv.writer(outputFile)
        for line in csvFileData:
            outputWriter.writerow(line)
        outputFile.close()

removeHeaderCsv('.')