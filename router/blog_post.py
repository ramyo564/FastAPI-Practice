from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/blog", tags=["blog"])


class BlogModal(BaseModel):
    title: str
    content: str
    nb_comments: int
    pubished: Optional[bool]


@router.post("/new/{id}")
def create_blog(blog: BlogModal, id: int, version: int = 1):
    return {"id": id, "data": blog, "version": version}
