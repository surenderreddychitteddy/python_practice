import xlrd

'''Reading Sheet1 of input excel sheet.'''
workbook = xlrd.open_workbook(input_file)
worksheet = workbook.sheet_by_name('Sheet1')
no_of_rows = worksheet.nrows
no_of_cols = worksheet.ncols

header, a_list, b_list, c_list = list(), list(), list(), list()

'''Appending header values(all columns of first row) to a list'''
for col in range(no_of_cols):
  data = worksheet.cell_value(0, col)
	header.append(data)

'''Assigning variables to the data in excel sheet'''

for row in range(1, no_of_rows): # First row is considered as header, Hence starting from second row
	for col in range(no_of_cols):
		data = worksheet.cell_value(row, col)
		''' Based on the index value assigning variable to the data fetched from Excel sheet. '''
		if col == 0:
			a_list.append(data)
		if col == 1:
			b_list.append(data)
		if col == 2:
			c_list.append(data)


