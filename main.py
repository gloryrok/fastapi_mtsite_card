# uvicorn main:app --reload     # was

import uvicorn

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates/")
app.mount("/static", StaticFiles(directory="static"), name="static")

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return{
        "message":"Hello FastAPI!"
    }

# 1.URL
#web 프로그래밍 기초 
# httpL//127.0.0.1:8000 = http/:localgost=8000
# 127.0.0.1과 localgost는 루프백 주소(현재 디바이스의 IP를 의미
# http -프로토콜를 제공하는 함수 ()
# 8000 - Port 번호
# http://127.0.0.1:8000/member?id=abc - 쿼리스트링(get)

# 숨겨야하는 정보들(post 방식)

