from tkinter import *
from tkinter.ttk import *
from time import *
#导入GUI库和时间库


win=Tk()                               #创建窗口
win.configure(bg='#000000')
win.attributes('-topmost',True)
win.attributes('-fullscreen',True)  
win.overrideredirect(True)             #设置窗口强制置顶，无边框，全屏
lt=Label(win,text="",background='#000000',foreground='#ffffff',font='consolas 100')  #创建显示时间的标签
lt.pack(expand=1,side='top')     #设置标签居中
exbutt=Button(win,text="Exit",command=exit)    #创建退出按钮
exbutt.pack(anchor='se')                   #设置退出按钮在右下角


def update_time():
    lt.config(text=strftime("%Y-%m-%d %H:%M:%S",localtime()))   #设置标签显示时间
    win.after(5,update_time)              #设置标签内容5毫秒刷新一次

update_time() 

win.mainloop()           