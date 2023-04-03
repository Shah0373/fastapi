from fastapi import APIRouter

router = APIRouter(
    tags=['Base']
)


@router.get("/")
def get_posts():
    return {"message": "Welcome to fastapi application!"}
