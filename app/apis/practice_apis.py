from fastapi import APIRouter

router = APIRouter()

@router.get("/practice")
def practice_handler():
    return {"message": "ok"}