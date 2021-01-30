import openpyxl
import pprint

print('We are going to open the workbook')
wb = openpyxl.load_workbook('censuspopdata.xlsx')

census_data = wb['Population by Census Tract']

#  1. Reads the data from the Excel spreadsheet
# 2. Counts the number of census tracts in each county
# 3. Counts the total population of each county
# 4. Prints the results
# This means your code will need to do the following:
# 1. Open and read the cells of an Excel document with the openpyxl module.
# 2. Calculate all the tract and population data and store it in a data structure.
# 3. Write the data structure to a text file with the .py extension using the pprint module.

countyData = {}

for row in range(2, census_data.max_row + 1):
    state = census_data['B' + str(row)].value
    county = census_data['C' + str(row)].value
    pop = census_data['D' + str(row)].value
    # print(f'State: {state} County: {county} and population:{pop}')
    countyData.setdefault(state, {})

    # we must be secure that the key exists, so we need to call the setdefault method to add the key or do nothing if it already exists
    # Since setdefault() will do nothing if the key already exists, you can call it on every iteration of the for loop without a problem.
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)
    

print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = '+pprint.pformat(countyData))
resultFile.close()
print('Done')
