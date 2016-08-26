#! /usr/bin/env python3
#coding=utf-8 
import matplotlib.pyplot as plt
from datetime import datetime,timedelta
import matplotlib.dates as mdate
import time
import sys


def readTxtFile(path):
    file=open(path,"r")
    rst=file.readlines()
    file.close()
    return rst

def work(filename):
    txt=readTxtFile(filename)
    times=[]
    values=[]
    ind=[]
    lbs=[]
    count=0
    for line in txt:
        line=line.strip('\n')
        if line=="": continue;
        arr=line.split(",")
        
        
        arr[0]=float(arr[0])
        ttime=time.localtime(arr[0])
        #arr[0]=ttime
        if count%60==0:
            ind.append(arr[0])
            lbs.append(time.strftime('%H:%M',ttime))
        count=count+1
        #print(arr[0])
        #print(arr)
        times.append(arr[0])
        values.append(int(arr[1]))
    #print(txt)
    #导入pyplot子库
    fig=plt.figure(figsize=(8, 6))
    #创建一个绘图对象, 并设置对象的宽度和高度, 如果不创建直接调用plot, Matplotlib会直接创建一个绘图对象

    ax1=fig.add_subplot(111)
    ax1.set_xticks(ind)
    ax1.set_xticklabels(lbs)
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
        pass
    #ax1.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
    #plt.xticks(times)


    plt.plot(times,values)
    #此处设置y的坐标为[1, 2, 3, 4], 则x的坐标默认为[0, 1, 2, 3]在绘图对象中进行绘图, 可以设置label, color和linewidth关键字参数
    plt.ylabel(ylabel)
    #给y轴添加标签, 给x轴加标签用xlable
    plt.title(title);
    plt.savefig(title+".png")
    #给2D图加标题
    plt.show()  #显示2D图


if __name__ == "__main__":
    args=sys.argv
    print(args)
    filename="douyuCount592227.txt"
    ylabel="count"
    title="people analyse"
    if(len(args)==3):
        filename=args[1]
        title=args[2]
    print("filename:",filename);
    work(filename);
