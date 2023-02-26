
import time
import requests
class Danmu():
    Hashmap = {}
    ans = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0
    }
    def __init__(self, room_id):
        # 弹幕url
        self.url = 'https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory'
        # 请求头
        self.headers = {
            'Host': 'api.live.bilibili.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
        }
        # 定义POST传递的参数
        self.data = {
            'roomid': room_id,
            'csrf_token': '',
            'csrf': '',
            'visit_id': '',
        }
        #self.log_file_write = open('danmu.log', mode='a', encoding='utf-8')
    def get_danmu(self):
        # 暂停0.5防止cpu占用过高
        time.sleep(0.5)
        # 获取直播间弹幕
        html = requests.post(url=self.url, headers=self.headers, data=self.data).json()
        # print(html)
        # 解析弹幕列表
        for content in html['data']['room']:
            # 获取昵称
            uid = str(content['uid'])
            # 获取发言
            #判断对应消息是否存在于哈希表中，如果和最后一条相同则打印并保存
            if uid in self.Hashmap:
                continue
            else:
                text = content['text']
                self.analyze_danmu(uid,text,self.ans)
                #self.Hashmap.setdefault(uid,0)
            # print(type(text))
            # if text[1]='a'
            # 获取发言时间 HH:mm:ss
            timeline = content['timeline'].split(" ")[1]
            # 记录发言
            msg = timeline + ' '+uid+" : " + text
            #print(msg)
            # print(msg)
        #     if msg + '\n' not in self.log:
        #         print(msg)
        #          # 打印消息
        #         # listb.insert(END, msg)
        #         # listb.see(END)
        #         # 保存日志
        #         self.log_file_write.write(msg + '\n')
        #         # 添加到日志列表
        #         self.log.append(msg + '\n')
        #     清空变量缓存
            nickname = ''
            text = ''
            timeline = ''
            msg = ''
        return self.ans
    #进行选项统计
    def analyze_danmu(self,uid,text,ans):
        text = text.upper()
        for ascll_value in range(65,70):
            if text.find(chr(ascll_value)) != -1:
                ans[chr(ascll_value)] += 1
                self.Hashmap.setdefault(uid, 0)
                return
            else:
                continue




# print("测试开始")
# roomId = input("输入房间号码")
if __name__ == '__main__':
    roomId = 26397089
    danmu = Danmu(roomId)
    while True:
        ans = danmu.get_danmu()
        print(ans)