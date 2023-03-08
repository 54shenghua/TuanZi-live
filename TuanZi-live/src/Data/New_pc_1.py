import asyncio
import zlib
from aiowebsocket.converses import AioWebSocket
import json

class Spider():
    Hashmap = {}
    ans = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0
    }
    


    def __init__(self, room_id):
        self.remote = 'ws://broadcastlv.chat.bilibili.com:2244/sub'
        self.roomid = str(room_id)  # input("输入房间号：")
        self.data_raw = '000000{headerLen}0010000100000007000000017b22726f6f6d6964223a{roomid}7d'
        self.data_raw = self.data_raw.format(headerLen=hex(27 + len(self.roomid))[2:],
                                             roomid=''.join(map(lambda x: hex(ord(x))[2:], list(self.roomid))))

    async def startup(self):
        
        async with AioWebSocket(self.remote) as aws:
            converse = aws.manipulator
            await converse.send(bytes.fromhex(self.data_raw))
            tasks = [self.receDM(converse), self.sendHeartBeat(converse)]
            await asyncio.wait(tasks)

    hb = '00 00 00 10 00 10 00 01  00 00 00 02 00 00 00 01'

    async def sendHeartBeat(self, websocket):
        while True:
            await asyncio.sleep(30)
            await websocket.send(bytes.fromhex(self.hb))
            # print('[Notice] Sent HeartBeat.')

    async def receDM(self, websocket):
        while True:
            recv_text = await websocket.receive()

            if recv_text == None:
                recv_text = b'\x00\x00\x00\x1a\x00\x10\x00\x01\x00\x00\x00\x08\x00\x00\x00\x01{"code":0}'

            self.printDM(recv_text)
        # 进行选项统计
    def analyze_danmu(self, uid, text, ans):
        text = text.upper()
        for ascll_value in range(65, 70):
            if text.find(chr(ascll_value)) != -1:
                ans[chr(ascll_value)] += 1
                self.Hashmap.setdefault(uid, 0)
                return
            else:
                continue
    # 将数据包传入：
    def printDM(self, data):
        # 获取数据包的长度，版本和操作类型
        packetLen = int(data[:4].hex(), 16)
        ver = int(data[6:8].hex(), 16)
        op = int(data[8:12].hex(), 16)

        # 有的时候可能会两个数据包连在一起发过来，所以利用前面的数据包长度判断，
        if (len(data) > packetLen):
            self.printDM(data[packetLen:])
            data = data[:packetLen]

        # 有时会发送过来 zlib 压缩的数据包，这个时候要去解压。
        if (ver == 2):
            data = zlib.decompress(data[16:])
            self.printDM(data)
            return

        # ver 为1的时候为进入房间后或心跳包服务器的回应。op 为3的时候为房间的人气值。
        if (ver == 1):
            if (op == 3):
                # print('[RENQI]  {}'.format(int(data[16:].hex(), 16)))
                pass
            return

        # ver 不为2也不为1目前就只能是0了，也就是普通的 json 数据。
        # op 为5意味着这是通知消息，cmd 基本就那几个了。
        if (op == 5):
            try:
                jd = json.loads(data[16:].decode('utf-8', errors='ignore'))
                if (jd['cmd'] == 'DANMU_MSG'):
                    #print('[DANMU] ', jd['info'][2], ': ', jd['info'][1])  # jd['info'][1]是弹幕内容   jd['info'][2][0]是uid
                    uid = jd['info'][2][0]
                    # 判断这个uid是否已经统计过
                    if uid in self.Hashmap:
                        pass
                    else:
                        text = jd['info'][1]
                        self.analyze_danmu(uid, text, self.ans)
                    #打印当前投票情况
                    
                    print(self.ans)
                    
                    # 将投票情况写入txt
                    # f = open('log.txt','a+',encoding='utf-8')
                    # f.write(str(self.ans)+'\n')
                    # f.close()
                elif (jd['cmd'] == 'SEND_GIFT'):
                    # print('[GITT]', jd['data']['uname'], ' ', jd['data']['action'], ' ', jd['data']['num'], 'x',
                    # jd['data']['giftName'])
                    pass
                elif (jd['cmd'] == 'LIVE'):
                    # print('[Notice] LIVE Start!')
                    pass
                elif (jd['cmd'] == 'PREPARING'):
                    # print('[Notice] LIVE Ended!')
                    pass
                else:
                    # print('[OTHER] ', jd['cmd'])
                    pass
            except Exception as e:
                pass

    async def running(self):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(await self.startup())
        except Exception as e:
            print("quite")

        
if __name__ == '__main__':
    roomId = 10267370
    danmu = Spider(roomId)
    danmu.running()