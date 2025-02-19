from api.v1.endpoints import auth
from api.v1.endpoints import users
from fastapi import APIRouter

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


router = APIRouter()
router.include_router(users.router)
router.include_router(auth.router)
