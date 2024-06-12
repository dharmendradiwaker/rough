import random
import pycron
import time
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

number_list = []

def get_number():
    n = 50
    random_number = random.randint(0, n-1)
    return random_number

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/numbers")
async def read_numbers():
    new_number = get_number()
    return {"random_number": new_number}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
