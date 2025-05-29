from typing import Optional
from fastapi import APIRouter, Query, Path, Body
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


@router.post("/new/{id}/comment")
def create_comment(
    blog: BlogModal,
    id: int,
    comment_id: int = Query(
        None,
        title="Id of the comment",
        description="Some description for comment_id",
        deprecated=True
        # alias="commentId",
    ),
):
    return {"blog": blog, "id": id, "comment_id": comment_id}
