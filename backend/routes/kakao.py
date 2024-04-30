from fastapi import APIRouter
router = APIRouter(
    tags=["kakao"],
)

@router.post("/")
async def send_message() -> dict:
    return{"status": {"code": 200, "message": "success"}}

app.include_router(kakao.router, prefix="/kakao")

@app.get("/") # http://127.0.0.1:8000
async def welcome(request:Request):
    return templates.TemplateResponse("index.html",{"request": request})