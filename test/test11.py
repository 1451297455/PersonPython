# test11.py
# coding:utf-8
import Tkinter
import sys
from tkinter import *
from win32api import GetSystemMetrics

# try:
#     from tkinter import *
# except ImportError:  # Python 2.x
#     PythonVersion = 2
#     # from Tkinter import *
#     # from tkFont import Font
#     # from ttk import *
#     # from tkMessageBox import *
#     # import tkFileDialog
# else:  # Python 3.x
#     PythonVersion = 3
#     from tkinter.font import Font
#     from tkinter.ttk import *
#     from tkinter.messagebox import *

height = GetSystemMetrics(0)
width = GetSystemMetrics(1)
print height

tk = Tkinter.Tk()
tk.title('Python GUI图形界面')
for item in ['时延app', '次数', 'case app', '次数', '其他配置']:
    Label(tk, text=item, bg='gray').pack(fill=X, anchor=N, ipadx=2, ipady=2, side=LEFT)
for item in ['SMS:', 'Dialer:', 'music:', 'wechat:']:
    # Label(tk, text='a').grid()
    Label(tk, text=item).pack()

    # label = Tkinter.Label(frame, text="Hello, World")
    # label.pack(fill=X, expand=1)
    Button(tk, text="Exit", command=tk.destroy).pack(side=BOTTOM)
    # button.pack(side=BOTTOM)
    tk.mainloop()
