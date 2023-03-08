from fastapi import FastAPI
from New_pc_1 import Spider
import uvicorn
from pydantic import BaseModel
import csv
import time
from wsgiref import headers
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI()
app.add_middleware(
        CORSMiddleware,

        allow_origins=["*"],

        allow_credentials=False,

        allow_methods=['*']
    )
class Options(BaseModel):
       options:list
       problemValue:str
       time:int
class PresetIndex(BaseModel):
       index:int
       

#定义全局所要用的变量
danmu=Spider(24471267)
ifStop=True
data = list()
options = dict()
runningTime = int()
preTime = float()
#读取预定义文件
preSteFile = open("preset.csv","r",encoding="UTF-8")
preSets = csv.reader(preSteFile)
preSetList = list(preSets)
print(preSetList)
#初始化日志文件
outcome = open("history.csv","w",newline='',encoding="UTF-8") 
headers=['question','A','B','C','D','E']
writers = csv.DictWriter(outcome,fieldnames=headers)
writers.writeheader
header = {'question':'question','A':'A','B':'B','C':'C','D':'D','E':'E'}
writers.writerow(header)


#开启爬虫
@app.get("/startPC")
async def StartPC():
       global danmu
       await danmu.running()
       return{
              "status":True,
       }
#开始
@app.post("/start")
async def Start():
       global ifStop 
       ifStop = False
       global danmu
       danmu.ans['A']=0
       danmu.ans['B']=0
       danmu.ans['C']=0
       danmu.ans['D']=0
       danmu.ans['E']=0
       danmu.Hashmap={}
       global preTime
       preTime = time.time()
       return{
              "status":True,
       }
#暂停（但不清除数据）
@app.post("/stop")
async def Stop():
        global data
        global ifStop
        global options
        ifStop = True
        recent_data = danmu.ans
        n=0
        data.clear()
        for key in options :
              if key=="question":
                     continue
              _data={}
              _data["label"]= options[key]
              _data["count"]= recent_data[chr(n+65)]
              data.append(_data)
              n=n+1
        a = {'question':options["question"],'A':recent_data['A'],'B':recent_data['B'],'C':recent_data['C'],'D':recent_data['D'],'E':recent_data['E']}
        writers.writerow(a)
        return{
              "status":True,
              "data":data
       }
#清除数据
@app.post("/reset")
async def Reset():
        global danmu
        danmu.ans['A']=0
        danmu.ans['B']=0
        danmu.ans['C']=0
        danmu.ans['D']=0
        danmu.ans['E']=0
        danmu.Hashmap={}
        global data
        data= []
        global options
        options = {}
        global ifStop 
        ifStop = True
        return{
               "status":True
        }
#admin面板将选项传入
@app.post("/inPutOptions")
async def InPutOptions(inPutOption:Options):
       global options
       global runningTime
       runningTime = inPutOption.time
       options["question"] = inPutOption.problemValue
       for pair in inPutOption.options:
              option = pair["option"]
              label =  pair['label']
              options[pair["option"]] = option +"   "+label
       return {
              "status":True,
       }
#char面板拿走选项
@app.get("/getOptions")
async def GetOptions():
       global options
       global runningTime
       return{
              "status":True,
              "options":options,
              "time":runningTime
       }
#传回爬虫数据
@app.get("/pc")
async def PC(): 
        global preTime
        global runningTime
        global ifStop
        global options
        global data
        if(ifStop):#在暂停时传回暂停时所储存的数据
               return {
                      "status":True,
                      "data":data
               }
        if (time.time() - preTime)>runningTime:
               ifStop = True
        recent_data = danmu.ans
        n=0
        data.clear()
        for key in options :
              if key=="question":
                     continue
              _data={}
              _data["label"]= options[key]
              _data["count"]= recent_data[chr(n+65)]
              data.append(_data)
              n=n+1
        return {
                      "status":True,
                      "data":data
               }

##预设问题选项读取
@app.get("/getPreset")
async def getPreset(index):
       _index = int(index)
       global preSetList
       preSet = dict()
       for a in range(0,7):
              if preSetList[_index][a] != "":
                     preSet[preSetList[0][a]]=preSetList[_index][a]

       return{
              "status":True,
              "data":preSet
       }
##关闭文件
@app.get("/exit")
async def exit():
       global outcome
       outcome.close
if __name__=='__main__':
       uvicorn.run (app) 