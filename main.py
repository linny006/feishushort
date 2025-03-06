from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse

app = FastAPI(title="飞书文档跳转服务")

FEISHU_URL = "https://vcn6qkr6n31j.feishu.cn/wiki/EW4IwwfmGiUB1Pk1rV2cUziUnve?from=from_copylink"

@app.get("/")
async def root():
    return RedirectResponse(url=FEISHU_URL)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
