from fastapi import FastAPI
import json
app = FastAPI()

#获得爬虫数据
import pachong
load=pachong.run()
if load=={}  :
    load["status"]="false"
else :
    load["status"]="ture"

@app.get("/houduan")
async def root():   
        return {str(load)}