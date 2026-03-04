from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.database import users_collection
from app.schemas.user_schema import UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


# CREATE
@router.post("/")
def create_user(user: UserCreate):
    if users_collection.find_one({"username": user.username}):
        raise HTTPException(400, "Username already exists")

    result = users_collection.insert_one(user.dict())
    return {"id": str(result.inserted_id)}


# READ ALL
@router.get("/")
def get_users():
    users = []
    for u in users_collection.find():
        users.append({
            "id": str(u["_id"]),
            "username": u["username"],
            "mobile": u["mobile"]
        })
    return users


# UPDATE
@router.put("/{user_id}")
def update_user(user_id: str, user: UserUpdate):
    result = users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {k: v for k, v in user.dict().items() if v}}
    )
    if result.matched_count == 0:
        raise HTTPException(404, "User not found")
    return {"message": "Updated"}


# DELETE
@router.delete("/{user_id}")
def delete_user(user_id: str):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(404, "User not found")
    return {"message": "Deleted"}