from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from bson import ObjectId
from bson.errors import InvalidId
from datetime import datetime, timezone, timedelta

from config.db import notes_collection
from schemas.note import noteEntity, notesEntity

note = APIRouter()
templates = Jinja2Templates(directory="templates")

# Define IST timezone (UTC +5:30)
IST = timezone(timedelta(hours=5, minutes=30))


# GET all notes (HTML)
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = notes_collection.find({})
    all_notes = notesEntity(docs)
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": all_notes})


# POST new note
@note.post("/")
def add_note(
        title: str = Form(...),
        desc: str = Form(...),
        important: bool = Form(False)
):
    created_at = datetime.now(IST)
    note_dict = {
        "title": title,
        "desc": desc,
        "important": important,
        "created_at": created_at,
        "updated_at": created_at  # Initially same as created_at
    }
    notes_collection.insert_one(note_dict)
    return RedirectResponse("/", status_code=303)


# GET edit note page
@note.get("/edit/{note_id}", response_class=HTMLResponse)
async def edit_note_page(request: Request, note_id: str):
    try:
        obj_id = ObjectId(note_id)
    except (InvalidId, TypeError):
        raise HTTPException(status_code=400, detail="Invalid note ID")

    note_doc = notes_collection.find_one({"_id": obj_id})
    if not note_doc:
        raise HTTPException(status_code=404, detail="Note not found")

    return templates.TemplateResponse(
        "edit_note.html",
        {"request": request, "note": noteEntity(note_doc)}
    )


# POST update note
@note.post("/edit/{note_id}")
async def update_note(
        note_id: str,
        title: str = Form(...),
        desc: str = Form(...),
        important: bool = Form(False)
):
    try:
        obj_id = ObjectId(note_id)
    except (InvalidId, TypeError):
        raise HTTPException(status_code=400, detail="Invalid note ID")

    updated_at = datetime.now(IST)  # Add timestamp for updates

    update_result = notes_collection.update_one(
        {"_id": obj_id},
        {"$set": {
            "title": title,
            "desc": desc,
            "important": important,
            "updated_at": updated_at  # Track when note was updated
        }}
    )

    if update_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")

    return RedirectResponse("/", status_code=303)


# DELETE note
@note.post("/delete/{note_id}")
async def delete_note(note_id: str):
    try:
        obj_id = ObjectId(note_id)
    except (InvalidId, TypeError):
        raise HTTPException(status_code=400, detail="Invalid note ID")

    result = notes_collection.delete_one({"_id": obj_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")

    return RedirectResponse("/", status_code=303)