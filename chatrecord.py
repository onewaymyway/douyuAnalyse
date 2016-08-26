import time, sys
import codecs
from danmu import DanMuClient

def pp(msg):
    print(msg.encode(sys.stdin.encoding, 'ignore').
        decode(sys.stdin.encoding))
    
def addMsg(msg):
    f=codecs.open("douyuChat"+roomID+".txt","a","utf-8");
    f.write('\n'+msg);
    f.close();

roomID="641207"

    
def begin():
    dmc = DanMuClient('http://www.douyu.com/'+roomID)
    if not dmc.isValid(): print('Url not valid')

    @dmc.danmu
    def danmu_fn(msg):
        pp('[%s] %s' % (msg['NickName'], msg['Content']))
        msg=",".join([str(time.time()),msg['NickName'], msg['Content']])
        addMsg(msg);

    @dmc.gift
    def gift_fn(msg):
        pp('[%s] sent a gift!' % msg['NickName'])
        msg=",".join([str(time.time()),msg['NickName'],"sent a gift!"])
        addMsg(msg);

    @dmc.other
    def other_fn(msg):
        pp('Other message received')
        
    dmc.start(blockThread = True)

    

if __name__ == "__main__":
    args=sys.argv
    print(args)
    if(len(args)==2):
        roomID=args[1]
    print("roomID:",roomID);
    begin();
