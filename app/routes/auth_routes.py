from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.config import ADMIN_USERNAME, ADMIN_PASSWORD
from app.utils.auth_utils import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

class LoginSchema(BaseModel):
    username: str
    password: str

@router.post("/login")
def admin_login(data: LoginSchema):
    if data.username != ADMIN_USERNAME or data.password != ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": data.username})
    return {"access_token": token, "token_type": "bearer"}

