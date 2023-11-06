from tkinter import *
from tkinter.ttk import *
from time import *
import config
#导入GUI库和时间库


win=Tk()                               #创建窗口
win.configure(bg=config.backColor)
win.attributes('-topmost',True)
if config.fullscreen:
    win.attributes('-fullscreen',True)
if config.overrideredirect:
    win.overrideredirect(True)             #设置窗口强制置顶，无边框，全屏
lt=Label(win,text="",background=config.backColor,foreground=config.foreColor,font=(config.font,str(config.font_size)))  #创建显示时间的标签
lt.pack(expand=1,side='top')     #设置标签居中
if config.haveExitbutt:
    exbutt=Button(win,text="Exit",command=win.quit)    #创建退出按钮
    exbutt.pack(anchor='se')                   #设置退出按钮在右下角


def update_time():
    lt.config(text=strftime(config.time_format,localtime()))   #设置标签显示时间
    win.after(config.uptime,update_time)              #设置标签内容5毫秒刷新一次

update_time() 

win.mainloop()           