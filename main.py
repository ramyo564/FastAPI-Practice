from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()


@app.get("/")
def index():
    return "Hello World!"


@app.get("/blog/all")
def get_all_bolg(page, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}


@app.get("/blog/{id}/comments/{comment_id}")
def get_comment(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = None
):
    return {
        "message": f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"
    }


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
