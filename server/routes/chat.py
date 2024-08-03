from fastapi import APIRouter

router = APIRouter(
    tags=["chat"],
)

router.websocket("/ws")
