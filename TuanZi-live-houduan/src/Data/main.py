from fastapi import FastAPI
from pc import Danmu
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class Options(BaseModel):
       options:list
       

#定义全局所要用的变量
danmu=Danmu(26397089)
ifStop=False
data = []
options = dict()
#开始
@app.post("/start")
async def Start():
       ifStop = False
       return{
              "status":True,
       }
#暂停（但不清除数据）
@app.post("/stop")
async def Stop():
        data = danmu.get_danmu()
        return{
              "status":True,
              "data":data
       }
#清除数据
@app.post("/reset")
async def Reset():
        danmu.ans['A']=0
        danmu.ans['B']=0
        danmu.ans['C']=0
        danmu.ans['D']=0
        danmu.ans['E']=0
        data = []
        danmu.Hashmap={}
        options = {}
        return{
               "status":True
        }
#admin面板将选项传入
@app.post("/inPutOptions")
async def InPutOptions(inPutOption:Options):
       options = inPutOption
       for pair in inPutOption:
               options[pair.option] = "{pair.option}  {pair.label}"
       return {
              "status":True,
       }
#char面板拿走选项
@app.get("/getOptions")
async def GetOptions():
       return{
              "status":True,
              "options":options
       }
#传回爬虫数据
@app.get("/pc")
async def PC(): 
        if(ifStop):#在暂停时传回暂停时所储存的数据
               return {
                      "status":True,
                      "Data":data
               }
        load=danmu.get_danmu()  
        return {
                      "status":True,
                      "Data":load
               }

if __name__=='__main__':
     uvicorn.run (app)  