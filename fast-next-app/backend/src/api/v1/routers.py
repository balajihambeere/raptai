from api.v1.endpoints import auth
from api.v1.endpoints import users
from fastapi import APIRouter

router = APIRouter()
router.include_router(users.router)
router.include_router(auth.router)
