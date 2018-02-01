import os
path = 'C:\Users\Jinchao_1.Zhang\Desktop\Pic_1'
pics = os.listdir(os.getcwd())
count = 1
for pic in pics:
	os.rename(os.path.join(path, pic), os.path.join(path, str(count) + ".jpg"))
	count += 1