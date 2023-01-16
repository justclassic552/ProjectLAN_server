from fastapi import FastAPI
import uvicorn
import time

app = FastAPI()

status = False


@app.get("/get_status")
async def handle_status():
    global status
    if status:
        status = False
        return {"status": True}
    return {"status": False}


@app.get("/switch_status")
async def handle_switch():
    global status
    status = True
    return {"status": status}


if __name__ == "__main__":
    while True:
        try:
            uvicorn.run(app, host="127.0.0.1", port=8000)
        except Exception as e:
            time.sleep(3)

