# coding:utf-8
import xlwt
import xlrd

doc = xlwt.Workbook()


def createconfig():
    global i, item, data
    docs = doc.add_sheet('config')
    docs.write(0, 0, 'app')
    docs.write(0, 1, 'runtimes')
    docs.write(0, 2, 'remark')
    config = open('D:\\config.ini', 'r')
    i = 1
    while True:
        item = config.readline()
        if item:
            if item.startswith('Time'):
                data = item.split(' ')
                docs.write(i, 0, data[1])
                docs.write(i, 1, data[3])
                docs.write(i, 2, data[4].decode('GBK'))
                i = i + 1
            else:
                data = item.split(' ')
                docs.write(i, 0, data[0])
                docs.write(i, 1, data[2])
                docs.write(i, 2, data[3].decode('GBK'))
                i = i + 1
        else:
            break


def createuninstallapp():
    global i, item, data
    docs = doc.add_sheet('uninstallapp')
    docs.write(0, 0, 'testapp')
    config = open('D:\\uninstalltest.ini', 'r')
    i = 1
    while True:
        item = config.readline()
        if item:
            docs.write(i, 0, item.strip())
            i = i + 1
        else:
            break


def createdev():
    global i, item, data
    docs = doc.add_sheet('device')
    docs.write(0, 0, 'devices')
    config = open('D:\\dev.ini', 'r')
    i = 0
    config.readline()
    item = config.readline()
    docs.write(1, 0, item.split()[0].strip())


def createuninstallapk():
    global i, item, data
    docs = doc.add_sheet('uninstallapk')
    docs.write(0, 0, 'testapp')
    config = open('D:\\uninstall apk.ini', 'r')
    i = 1
    while True:
        item = config.readline()
        if item:
            docs.write(i, 0, item.strip())
            i = i + 1
        else:
            break


def createtestapp():
    global i, item, data
    docs1 = doc.add_sheet('test_app')
    docs1.write(0, 0, 'app')
    docs1.write(0, 1, 'times')
    docs1.write(0, 2, 'pack/activity')
    config1 = open('D:\\Test_app.ini', 'r')
    i = 1
    while True:
        item = config1.readline()
        if item:
            if item.startswith('Time'):
                data = item.split(' ')
                docs1.write(i, 0, data[1].strip())
                docs1.write(i, 1, data[3].strip())
            elif item.startswith('Pack/Activity'):
                data = item.split(' ')
                docs1.write(i, 2, data[1].strip())
            else:
                i = i + 1
                pass
        else:
            break


def readconfig(xls):
    dev = xls.sheet_by_name('config')
    line2 = dev.nrows
    # applist = []
    for a in range(1, line2):
        if dev.cell_value(a, 0) == 'Youku':
            print dev.cell_value(a, 1)
        else:
            continue


def readtestapp(xls):
    dev = xls.sheet_by_name('test_app')
    rows = dev.nrows
    for a in range(1, rows):
        name = dev.cell_value(a, 0)
        times = dev.cell_value(a, 1)
        activity = dev.cell_value(a, 2)
        print name + ':' + times + ':' + activity


def readuninstallapp(xls):
    dev = xls.sheet_by_name('uninstallapp')
    rows = dev.nrows
    for a in range(1, rows):
        print dev.cell_value(a, 0)


def readdevices(xls):
    dev = xls.sheet_by_name('device')
    rows = dev.nrows
    for a in range(1, rows):
        print dev.cell_value(a, 0)


def main():
    createdev()
    createconfig()
    createtestapp()
    createuninstallapp()
    createuninstallapk()
    doc.save('config.xls')

    xls = xlrd.open_workbook('config.xls')

    readconfig(xls)
    readtestapp(xls)
    readuninstallapp(xls)
    readdevices(xls)


if __name__ == '__main__':
    main()
