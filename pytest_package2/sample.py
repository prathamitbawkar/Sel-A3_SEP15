
import xlrd

path = r'C:\Users\prath\OneDrive\Desktop\dd_001.xlsx'

# open the excel
wb = xlrd.open_workbook(path)
# print(wb)

# open the worksheet
ws = wb.sheet_by_name('test') # sheet object
# print(ws)

rows = ws.get_rows()
print(rows)    # generator object


for ele in rows:
    print(ele[0].value,ele[1].value,ele[2].value,ele[3].value)

