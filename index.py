from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.note import note
import os

app = FastAPI()

# Serve static files only if folder is not empty
if os.path.isdir("static") and os.listdir("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routes
app.include_router(note)

# Health check endpoint
@app.get("/ping")
async def ping():
    return {"message": "Server is running!"}
