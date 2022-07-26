from typing import Optional  # Typing모듈의 Optional 사용
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/{item_id}")
def read_item(item_id: str, q: Optional[str] = None):  # Optional임을 명시하는 게 좋다.
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
