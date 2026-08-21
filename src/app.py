from pathlib import Path
import shutil

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(BASE_DIR / "index.html")


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    filename = Path(file.filename or "upload").name
    destination = UPLOAD_DIR / filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "uploaded", "filename": filename}
