from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.note import note

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routes
app.include_router(note)

# Health check endpoint
@app.get("/ping")
async def ping():
    return {"message": "Server is running!"}
