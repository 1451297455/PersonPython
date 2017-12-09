import os
import xlwt
import xlrd
import sys

apks = []
docs = xlwt.Workbook()

def creatxls(docs):
    doc = docs.add_sheet('pack')
    doc.write(0, 0, 'app')
    doc.write(0, 1, 'appname')
    doc.write(0, 2, 'pack')
    doc.write(0, 3, 'activity')
    return doc


def getapk():
    files = os.listdir(os.getcwd())
    for item in files:
        if item.endswith(".apk"):
            apks.append(item)
        else:
            continue


def setdate(doc):
    i = 1
    for apk in apks:
        doc.write(i, 0, apk)
        details = os.popen('aapt dump badging ' + apk)
        while True:
            detail = details.readline()
            if detail and detail.startswith('package'):
                doc.write(i, 2, detail.strip().split(' ')[1].split('\'')[1])
            elif detail and detail.startswith('application:'):
                doc.write(i, 1, detail.strip().split('\'')[1].decode('utf-8'))
            elif detail and detail.startswith('launchable-activity'):
                doc.write(i, 3, detail.strip().split(' ')[1].split('\'')[1])
            elif detail:
                continue
            else:
                i = i + 1
                break
    docs.save('app.xls')

if __name__=='__main__':
    getapk()
    setdate(creatxls(docs))
