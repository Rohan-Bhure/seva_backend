from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.database import sevas_collection
from app.schemas.seva_schema import SevaCreate, SevaUpdate

router = APIRouter(prefix="/sevas", tags=["Sevas"])


# CREATE
@router.post("/")
def create_seva(seva: SevaCreate):
    if sevas_collection.find_one({
        "category": seva.category,
        "subcategory": seva.subcategory
    }):
        raise HTTPException(400, "This seva already exists")

    result = sevas_collection.insert_one(seva.dict())
    return {"id": str(result.inserted_id)}


# READ ALL
@router.get("/")
def get_sevas():
    sevas = []
    for s in sevas_collection.find():
        sevas.append({
            "id": str(s["_id"]),
            "category": s["category"],
            "subcategory": s["subcategory"]
        })
    return sevas


# UPDATE
@router.put("/{seva_id}")
def update_seva(seva_id: str, seva: SevaUpdate):
    result = sevas_collection.update_one(
        {"_id": ObjectId(seva_id)},
        {"$set": {k: v for k, v in seva.dict().items() if v}}
    )
    if result.matched_count == 0:
        raise HTTPException(404, "Seva not found")
    return {"message": "Updated"}


# DELETE
@router.delete("/{seva_id}")
def delete_seva(seva_id: str):
    result = sevas_collection.delete_one({"_id": ObjectId(seva_id)})
    if result.deleted_count == 0:
        raise HTTPException(404, "Seva not found")
    return {"message": "Deleted"}