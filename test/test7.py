# test7.py
# coding:utf-8
from test4 import createdev
from datetime import datetime
import logging
import sys
import xlrd
import os

reload(sys)
sys.setdefaultencoding('utf-8')
docs = xlrd.open_workbook('total.xls')
dev = docs.sheet_by_name('sheet1')
rows = dev.nrows
print rows
os.system('echo Large cycle = 1  //大循环次数 >config.ini')
os.system('echo ################################################################ >>config.ini')
row = 1
while True:
    if row < rows or row == rows:
        os.system('echo APKL ' + dev.cell_value(row, 0) + ' = ' + str(dev.cell_value(row, 1)).replace(' ',
                                                                                                      '_') + '>>config.ini')
        os.system('echo Time ' + str(dev.cell_value(row, 1)).replace(' ', '_') + ' = 5   //次数>>config.ini')
        os.system('echo AppName = ' + str(dev.cell_value(row, 1)).replace(' ', '_') + '  //控件标识>>config.ini')
        os.system('echo Pack/Activity ' + dev.cell_value(row, 6) + '>>config.ini')
        os.system('echo ################################################################ >>config.ini')
        row = row + 1
    else:
        break
