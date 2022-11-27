from fastapi import FastAPI
from pc import Danmu
import uvicorn
from pydantic import BaseModel
<<<<<<< Updated upstream
=======
import csv
import time
from wsgiref import headers
>>>>>>> Stashed changes

app = FastAPI()

class Options(BaseModel):
       options:list
<<<<<<< Updated upstream
       

#定义全局所要用的变量
danmu=Danmu(25868330)
ifStop=False
data = []
options = dict()
#开始
@app.post("/start")
async def Start():
       ifStop = False
=======
       problemValue:str
       time:int
class PresetIndex(BaseModel):
       index:int
       

#定义全局所要用的变量
danmu=Danmu(6925055)
ifStop=True
data = dict()
options = dict()
runningTime = int()
preTime = float()
#读取预定义文件
preSteFile = open("preset.csv","r",encoding="UTF-8")
preSets = csv.reader(preSteFile)
preSetList = list(preSets)
print(preSetList)
#初始化日志文件
outcome = open("history.csv","w",encoding="UTF-8") 
headers=['question','A','B','C','D','E']
writers = csv.DictWriter(outcome,fieldnames=headers)
writers.writeheader
header = {'question':'question','A':'A','B':'B','C':'C','D':'D','E':'E'}
writers.writerow(header)
#开始
@app.post("/start")
async def Start():
       global ifStop 
       ifStop = False
       global preTime
       preTime = time.time()
>>>>>>> Stashed changes
       return{
              "status":True,
       }
#暂停（但不清除数据）
@app.post("/stop")
async def Stop():
<<<<<<< Updated upstream
        data = danmu.get_danmu()
=======
        global data
        global ifStop
        ifStop = True
        data = danmu.get_danmu()
        a = {'question':'asdf','A':data['A'],'B':data['B'],'C':data['C'],'D':data['D'],'E':data['E']}
        writers.writerow(a)
>>>>>>> Stashed changes
        return{
              "status":True,
              "data":data
       }
#清除数据
@app.post("/reset")
async def Reset():
<<<<<<< Updated upstream
=======
        global danmu
>>>>>>> Stashed changes
        danmu.ans['A']=0
        danmu.ans['B']=0
        danmu.ans['C']=0
        danmu.ans['D']=0
        danmu.ans['E']=0
<<<<<<< Updated upstream
        data = []
        danmu.Hashmap={}
        options = {}
=======
        danmu.Hashmap={}
        global data
        data= {}
        global options
        options = {}
        global ifStop 
        ifStop = True
>>>>>>> Stashed changes
        return{
               "status":True
        }
#admin面板将选项传入
@app.post("/inPutOptions")
async def InPutOptions(inPutOption:Options):
<<<<<<< Updated upstream
       options = inPutOption
       for pair in inPutOption:
               options[pair.option] = "{pair.option}  {pair.label}"
=======
       global options
       global runningTime
       runningTime = inPutOption.time
       options["question"] = inPutOption.problemValue
       for pair in inPutOption.options:
              option = pair["option"]
              label =  pair['label']
              options[pair["option"]] = option +"   "+label
>>>>>>> Stashed changes
       return {
              "status":True,
       }
#char面板拿走选项
@app.get("/getOptions")
async def GetOptions():
<<<<<<< Updated upstream
=======
       global options
>>>>>>> Stashed changes
       return{
              "status":True,
              "options":options
       }
#传回爬虫数据
@app.get("/pc")
async def PC(): 
<<<<<<< Updated upstream
=======
        global preTime
        global runningTime
        global ifStop
>>>>>>> Stashed changes
        if(ifStop):#在暂停时传回暂停时所储存的数据
               return {
                      "status":True,
                      "Data":data
               }
<<<<<<< Updated upstream
=======
        if (time.time() - preTime)>runningTime:
               ifStop = True
>>>>>>> Stashed changes
        load=danmu.get_danmu()  
        return {
                      "status":True,
                      "Data":load
               }

<<<<<<< Updated upstream
=======
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
              "Data":preSet
       }
       
>>>>>>> Stashed changes
if __name__=='__main__':
     uvicorn.run (app)  