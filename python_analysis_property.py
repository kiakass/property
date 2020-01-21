import pandas as pd
import xlwings as xw

path = r'f:\data\kb\★(월간)KB주택가격동향_시계열(2019.12).xlsx'
wb = xw.Book(path)
sheet = wb.sheets['매매종합']
row_num = sheet.range(1,1).end('down').end('down').end('down').row
data_range = 'A2:GE' + str(row_num)

raw_data = sheet[data_range].options(pd.DataFrame, index=False, header=True).value
print(raw_data)
#raw_data = pd.read_excel(path, sheet_name='매매종합')
