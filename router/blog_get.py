from router.blog_post import required_functionality
from fastapi import APIRouter, status, Response, Depends
from enum import Enum
from typing import Optional

router = APIRouter(prefix="/blog", tags=["blog"])


@router.get(
    "/all",
    summary="Retrieve all blogs",
    description="This api call simulates fetching all blogs",
    response_description="The list of available blogs",
)
def get_blogs(
    page,
    page_size: Optional[int] = None,
    req_parameter: dict = Depends(required_functionality),
):
    return {"message": f"All {page_size} blogs on page {page}", "req": req_parameter}


@router.get("/{id}/comments/{comment_id}", tags=["comment"])
def get_comment(
    id: int,
    comment_id: int,
    valid: bool = True,
    username: Optional[str] = None,
    req_parameter: dict = Depends(required_functionality),
):
    """
    Simulates retrieving a comment of a blog

    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional quey parameter
    """
    return {
        "message": f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"
    }


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howTo = "howTo"


@router.get("/type/{type}")
def get_bolg_type(
    type: BlogType,
    req_parameter: dict = Depends(required_functionality),
):
    return {"message": f"Blog type {type.value}"}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_bolg(
    id: int,
    response: Response,
    req_parameter: dict = Depends(required_functionality),
):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id {id}"}
