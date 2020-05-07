import xlrd

# work_book = xlrd.open_workbook("TestTable.xls")
# print(work_book, type(work_book))
# sheets = work_book.sheets()
# print(sheets, type(sheets))
#
# usedSheet = None
#
# for sheet in sheets:
#     if sheet.name == "TestSheet":
#         usedSheet = sheet
#         print(sheet.name + ": 我就是你想要的")
#     else:
#         print(sheet.name + ": 我就是你不想要的")
#
# print("obtained sheet: " + usedSheet.name)

# obtain a sheet in excel
def Getsheetbysheetname(excelName, sheetName):
    work_book = xlrd.open_workbook(excelName)
    sheets = work_book.sheets()

    tmpSheet = None

    for sheet in sheets:
        if sheet.name == sheetName:
            tmpSheet = sheet
            print(sheet.name + ": 我就是你想要的")
        else:
            print(sheet.name + ": 我就是你不想要的")

    return tmpSheet



# obtain a sum for a specific column and row ranges
def calculateSum (colIndex, rowStart, rowEnd, sheet):
    sum=0
    for i in range (rowStart, rowEnd):
        rowValues = sheet.row(i)
        sum+=float(rowValues[colIndex].value)
    return sum


usedSheet = Getsheetbysheetname("TestTable.xls", "TestSheet")
money_sum=calculateSum(1, 3, 15, usedSheet)

print("sum_money", money_sum)

rate_sum = calculateSum(3, 3,15, usedSheet)
print("rate_sum", rate_sum)






# print("rows:" + str(usedSheet.nrows))
# print("cloumn:" + str(usedSheet.ncols))
#
# print(usedSheet.row(1))
#
# # for i in range(0,usedSheet.nrows):
# #     # row numbers
# #     print("rows"+str(i))
# #     # contents
# #     print(usedSheet.row(i))
#
# rowCount = usedSheet.nrows - 2
# print("real row count: " + str(rowCount))
#
# money_sum = 0
# for i in range(2, usedSheet.nrows):
#     rowValues = usedSheet.row(i)
#     # 注意方括号是指定那一列
#     print("money: " + str(rowValues[1].value))
#     money_sum += float(rowValues[1].value)
#
# print("monsum: " + str(money_sum))
#
# print("mean:" + str(money_sum / rowCount))
#
# rateSum = 0
#
# for i in range(2, usedSheet.nrows):
#     rowValues = usedSheet.row(i)
#     rateValue = rowValues[3].value
#     rateSum += float(rateValue)
#
# print("rateSum: ", str(rateSum))
#
# arrearsSum = 0
#
# for i in range(2, usedSheet.nrows):
#     rowValues = usedSheet.row(i)
#     arrearsValue = rowValues[-3].value
#     # arrearsValue = rowValues[11].value
#     arrearsSum += float(arrearsValue)
#
# print("arrearsSum: ", str(arrearsSum))







