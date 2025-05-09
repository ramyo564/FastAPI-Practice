from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/")
def index():
    return "Hello World!"


@app.get("/blog/all")
def get_all_bolg(page, page_size):
    return {"message": f"All {page_size} blogs on page {page}"}


@app.get("/blog/{id}")
def get_bolg(id: int):
    return {"message": f"Blog with id {id}"}


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howTo = "howTo"


@app.get("/blog/type/{type}")
def get_bolg_type(type: BlogType):
    return {"message": f"Blog type {type.value}"}
