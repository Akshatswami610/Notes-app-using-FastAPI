from pydantic import BaseModel
from datetime import datetime, timezone, timedelta

# Define IST timezone
IST = timezone(timedelta(hours=5, minutes=30))

class Note(BaseModel):
    title: str
    desc: str
    important: bool = False


def noteEntity(item) -> dict:
    created_at = item.get("created_at")

    # Handle datetime
    if isinstance(created_at, datetime):
        # Convert to IST if necessary
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=IST)
        else:
            created_at = created_at.astimezone(IST)
        formatted_time = created_at.strftime("%d-%m-%Y %H:%M")

    # Handle old string-based timestamps (e.g., "20:07")
    elif isinstance(created_at, str) and len(created_at) <= 5:
        formatted_time = f"Unknown Date {created_at}"  # Or just use the time as is
    else:
        formatted_time = ""

    return {
        "_id": str(item.get("_id", "")),
        "title": item.get("title", ""),
        "desc": item.get("desc", ""),
        "important": item.get("important", False),
        "created_at": formatted_time
    }


def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]
