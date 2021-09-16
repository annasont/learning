'''readCensusExc.py reads data from Excel spreadsheet, counts the number of census tracts in each county,
counts the total population for each county, prints the result to the new python-file.'''

import openpyxl, pprint
print('Opening workbook')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

print('Calculating...')
for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

countyDataFile = open('countyData.txt', 'w')

print('Writing result to "countyData.py" file')
countyDataFile = open('countyData.py', 'w')
countyDataFile.write('allData = ' + pprint.pformat(countyData))
countyDataFile.close()

print('Done!')