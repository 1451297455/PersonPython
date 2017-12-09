import xlrd
import os

xls = xlrd.open_workbook('total.xls')
dev = xls.sheet_by_name("sheet2")
x = dev.nrows
for a in x:
    str = dev.cell_value(a,1)
    ass = str.encode('unicode-escape').decode('string_escape')
    os.system('adb uninstall ' + ass)
