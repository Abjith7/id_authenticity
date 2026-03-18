from fastapi import FastAPI, UploadFile
import shutil
import os
import uuid

from tamper_check import detect_tampering
from ocr import extract_text
from rag_engine import generate_report

app = FastAPI()

os.makedirs("uploads", exist_ok=True)


@app.post("/analyze")
async def analyze(file: UploadFile):

    if not file.filename.lower().endswith(("png","jpg","jpeg")):
        return {"error": "Invalid image format"}

    filename = f"{uuid.uuid4()}.jpg"
    path = f"uploads/{filename}"

    try:

        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        tamper = detect_tampering(path)

        text = extract_text(path)

        report = generate_report(tamper, text)

        return {
            "tamper_check": tamper,
            "ocr_text": text,
            "fraud_report": report
        }

    except Exception as e:

        return {
            "error": str(e)
        }