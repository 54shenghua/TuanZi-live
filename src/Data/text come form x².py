#通过gethistory进行的弹幕爬取实验，gethistory每次申请只有十条弹幕数据
import requests,json,os,time
def main():
   #创建一个文件夹储存弹幕数据
   if os.path.exists('./data_package') == False:
      os.mkdir('./data_package')
   else:
      pass
   for i in range(0,9):#循环次数应设置为可控的，当用户按下停止按钮时就可以停止爬取,然后进行清空操作
      getdata(i)
      analyze(i)
      #time.sleep(15)#时间到时候具体调，假如后面提到的uid_voted的那个方法可行的话这里其实不用休眠了

def getdata(i):
   i = i
   #此url是固定的，只需更改roomid
   url = 'https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory'
   #UA伪装
   header = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26'
   }
   #url的参数
   param = {
      'roomid':42062
   }
   #请求json数据
   response = requests.get(url = url,params = param,headers = header).json()
   #将json数据保存到本地备用
   with open('./data_package/Danmu' + str(i) + '.json','w',encoding='utf-8') as fp:
      json.dump(response,ensure_ascii=False,fp = fp)

#记录已投票的uid,考虑到会重复读取一些弹幕，为避免重复计数，可能需要将uid_voted保存到本地，这样可以每读取一个弹幕文件都可以调用uid_voted进行比对,或是像现在这样将其作为全局变量统一记录
uid_voted = []
#统计选项
option_a,option_b,option_c,option_d = 0,0,0,0
def analyze(i):
   global uid_voted,option_a,option_b,option_c,option_d
   # 读取json数据
   i = i
   with open('./data_package/Danmu' + str(i) + '.json', 'r', encoding='utf-8') as fp:
      fp_load = json.load(fp)
      #将每一个人的弹幕取出来进行分析
      for index in range(len(fp_load['data']['room'])):
         print(fp_load['data']['room'][index]['text'] + '   ',end = '')#这些打印的东西到时候可以删掉，只是现在为了测试方便打出来看看
         text = fp_load['data']['room'][index]['text']
         uid = fp_load['data']['room'][index]['uid']
         #判断部分还需要改，这里做测试用
         if (text == 'A' or text == 'a') and uid not in uid_voted:
            option_a += 1
            uid_voted.append(uid)
         elif (text == 'B' or text == 'b') and uid not in uid_voted:
            option_b += 1
            uid_voted.append(uid)
         elif (text == 'C' or text == 'c') and uid not in uid_voted:
            option_c += 1
            uid_voted.append(uid)
         elif (text == 'D' or text == 'd') and uid not in uid_voted:
            option_d += 1
            uid_voted.append(uid)
         else:
            continue
      print('\n')
      print(option_a,option_b,option_c,option_d,sep = '  ')#这些打印的东西到时候可以删掉，只是现在为了测试方便打出来看看
      print(uid_voted)#这些打印的东西到时候可以删掉，只是现在为了测试方便打出来看看

main()
input()