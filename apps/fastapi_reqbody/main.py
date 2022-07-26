from typing import Optional
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# 1.Pydantic으로 Request Body 데이터 정의
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# 2.Type inting으로 위에서 생성한 Item Class 주입
# 3.Request Body 데이터를 Validation
@app.post("/items/")
def create_item(item: Item):
    return item

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
