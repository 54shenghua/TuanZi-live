from fastapi import FastAPI
from pc import Danmu
app = FastAPI()

#获得爬虫数据
danmu=Danmu(26397089)

@app.get("/pc")
async def root(): 
        load=danmu.get_danmu()  
        return load
@app.post("/stop")
async def root():
        danmu.ans['A']=0
        danmu.ans['B']=0
        danmu.ans['C']=0
        danmu.ans['D']=0
        danmu.ans['E']=0
        danmu.Hashmap={}