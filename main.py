from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "Hello World!"


@app.get("/blog/{id}")
def get_bolg(id: int):
    return {"message": f"Blog with id {id}"}


@app.get("/blog/all")
def get_all_bolg():
    return {"message": "All Blogs"}
