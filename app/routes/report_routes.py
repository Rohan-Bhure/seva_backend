from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from datetime import datetime
from openpyxl import Workbook
from app.database import submissions_collection

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/{date}")
def download_report(date: str):
    
    try:
        selected_date = datetime.strptime(date, "%Y-%m-%d").date()
    except:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")

    # Get submissions for that date
    records = submissions_collection.find({"date": str(selected_date)})

    data = list(records)

    if not data:
        raise HTTPException(status_code=404, detail="No submissions found for this date")

    # Create Excel
    wb = Workbook()
    ws = wb.active
    ws.title = "Seva Report"

    # Header
    ws.append(["Category", "Subcategory", "Done By", "Date"])

    # Rows
    for r in data:
        ws.append([
            r["category"],
            r["subcategory"],
            r["username"],
            r["date"]
        ])

    # Save file
    filename = f"seva_report_{date}.xlsx"
    filepath = f"/tmp/{filename}"

    wb.save(filepath)

    return FileResponse(
        filepath,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=filename
    )