from typing import Optional, List
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


@router.post("/new/{id}/comment/{comment_id}")
def create_comment(
    blog: BlogModal,
    id: int,
    comment_title: int = Query(
        None,
        title="Title of the comment",
        description="Some description for comment_title",
        deprecated=True,
        alias="commentTitle",
    ),
    # content: str = Body("Hi how are you"),                  <- default pamareters
    # content: str = Body(Ellipsis),                          <- non-optional pamareters
    # content: str = Body(...),                               <- non-optional pamareters
    # content: str = Body(..., min_length=10, max_length=20), <- Require min, max length
    content: str = Body(..., min_length=10, max_length=50, regex="^[a-z\s]*$"),
    # v: Optional[List[str]] = Query(None),                   <= Define an Optional query parameter
    v: Optional[List[str]] = Query(["1.0", "1.1", "1.2"]),
    comment_id: int = Path(..., gt=5, le=10)
):
    return {
        "blog": blog,
        "id": id,
        "comment_title": comment_title,
        "content": content,
        "version:": v,
        "comment_id": comment_id,
    }
