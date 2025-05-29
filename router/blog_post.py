from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/blog", tags=["blog"])


class BlogModal(BaseModel):
    title: str
    content: str
    nb_comments: int
    pubished: Optional[bool]


@router.post("/new")
def create_blog(blog: BlogModal):
    return {"data": blog}
