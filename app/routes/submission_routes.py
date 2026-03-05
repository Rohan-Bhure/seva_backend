from fastapi import APIRouter, HTTPException
from datetime import datetime
from bson import ObjectId
from app.database import submissions_collection
from app.schemas.submission_schema import SubmissionCreate

router = APIRouter(prefix="/submissions", tags=["Submissions"])


# CREATE SUBMISSION
@router.post("/")
def create_submission(data: SubmissionCreate):

    # convert date to string
    date_str = data.date.isoformat()

    existing = submissions_collection.find_one({
        "category": data.category,
        "subcategory": data.subcategory,
        "date": date_str
    })

    if existing:
        return {
            "message": "Already submitted",
            "done_by": existing["username"]
        }

    submission_data = data.dict()
    submission_data["date"] = date_str
    submission_data["createdAt"] = datetime.utcnow()

    result = submissions_collection.insert_one(submission_data)

    return {
        "id": str(result.inserted_id),
        "message": "Submission successful"
    }


# GET SUBMISSIONS BY DATE
@router.get("/{date}")
def get_submissions_by_date(date: str):

    submissions = []

    for s in submissions_collection.find({"date": date}):
        submissions.append({
            "category": s["category"],
            "subcategory": s["subcategory"],
            "username": s["username"],
            "date": s["date"]
        })

    return submissions