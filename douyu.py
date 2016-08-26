#! /usr/bin/env python3
#coding=utf-8
import urllib.parse
import urllib.request
import json
import time
import socket
import sys
import codecs

roomID="833617"
def getInfo():

    turl="http://open.douyucdn.cn/api/RoomApi/room/"+roomID
    
    req = urllib.request.Request(turl)
    #req = urllib.request.Request(turl)
    response = urllib.request.urlopen(req)
    the_page = response.read().decode("utf8")
    #print("the_page",the_page);
    jsonData=json.loads(the_page);
    jsonData=jsonData["data"]
    info=",".join([str(time.time()),str(jsonData["online"])])

    print(info)
    f=codecs.open("douyuCount"+roomID+".txt","a");
    f.write('\n'+info);
    f.close();

def loopWork():
    while(1):
        try:
            getInfo();
            #break
        except:
            print('error')
        time.sleep(5)
if __name__ == "__main__":
    args=sys.argv
    print(args)
    if(len(args)==2):
        roomID=args[1]
    print("roomID:",roomID);
    loopWork();
