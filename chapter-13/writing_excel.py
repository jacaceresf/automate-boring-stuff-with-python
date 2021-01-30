import openpyxl
import census2010

wb = openpyxl.Workbook()

for state, county in census2010.allData.items():
    # create a sheet for every state

    sheet_idx = 0

    print(f'Going to iterate over [{state}] results')

    wb.create_sheet(index=sheet_idx, title=state)
    sheet_idx += 1
    state_sheet = wb[state]
    state_sheet['A1'] = 'County'
    state_sheet['B1'] = 'Population'
    state_sheet['C1'] = 'Tracts'

    # fill in with its county data
    idx = 1
    for county_, data in county.items():
        idx += 1
        print(f'Got county [{county_}] and its census data [{data}')
        state_sheet['A'+str(idx)] = county_
        state_sheet['B'+str(idx)] = data['pop']
        state_sheet['C'+str(idx)] = data['tracts']
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

wb.save('census_to_excel.xlsx')
