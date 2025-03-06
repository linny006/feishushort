from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse

app = FastAPI(title="飞书文档跳转服务")

FEISHU_URL = "hhttps://iqzeljuzeco.feishu.cn/wiki/LmpcwCrImiQ1ANkqw6ScRB6dnJd"

@app.get("/")
async def root():
    return RedirectResponse(url=FEISHU_URL)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
