# coding:utf-8
import xlwt
import os

# 定义log日志列表
files = []

filelist = os.listdir(os.getcwd())
for fileitem in filelist:
	if fileitem.endswith('.log'):
		files.append(fileitem)


def creatxls(docs):
	doc = docs.add_sheet('sheet1')
	doc.write(0, 0, 'time')
	doc.write(0, 1, 'app')
	doc.write(0, 2, '1')
	doc.write(0, 3, '2')
	doc.write(0, 4, '3')
	doc.write(0, 5, '4')
	doc.write(0, 6, '5')
	doc.write(0, 7, '6')
	doc.write(0, 8, '7')
	doc.write(0, 9, '8')
	doc.write(0, 10, '9')
	doc.write(0, 11, '10')
	return doc


for logfile in files:
	docs = xlwt.Workbook()
	doc = creatxls(docs)
	comment = open(logfile, 'r')
	i = 0
	j = 2
	asum = 0
	while True:
		logs = comment.readline()
		if logs:
			if logs.startswith('20'):
				i = i + 1
				j = 2
				asum = 0
				testtime = logs.split(' ')[0]
				testname = logs.split(' ')[2]
				doc.write(i, 0, testtime)
				doc.write(i, 1, testname.encode('unicode-escape').decode('string_escape'))
				continue
			elif logs.startswith('WaitTime:'):
				delaytime = logs.split(' ')[1]
				doc.write(i, j, int(delaytime))
				asum = asum + int(delaytime)
				j = j + 1
				continue
		else:
			name = str(logfile).split('.')[0]
			docs.save(name + '.xls')
			break
