import xlwings as xw

wb = xw.Book("C:\\Users\\acer\\Desktop\\compare.xlsx")
sheet = wb.sheets["Sheet1"]

# Read data from column A (starting from row 1)
data_column_A = sheet.range('A2').expand('down').value
data_column_B = sheet.range('B2').expand('down').value

#print(data_column_A)
#print("------------")
#print(data_column_B)

cleaned_data_column_B = []

for i in data_column_B:
    try:
        cleaned_data_column_B.append(float(i))

    except:
        cleaned_data_column_B.append(i)

# print(cleaned_data_column_B)
# print("----------------------------")
# print(data_column_A)

column_A = []
column_B= []

_A =[]
_B =[]
for i in data_column_A:
    if type(i) == float:
        column_A.append(i)
    else:
        _A.append(i)
for i in cleaned_data_column_B:
    if type(i) == float:
        column_B.append(i)
    else:
        _B.append(i)
print(len(column_A))
print(len(column_B))
print(len(_A))
print(len(_B))

column_A.sort()
column_B.sort()

# Data to be written to column B
sheet.range("C2").options(transpose=True).value = column_A
sheet.range("D2").options(transpose=True).value = column_B





                                     
                                     