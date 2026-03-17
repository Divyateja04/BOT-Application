from fastapi import FastAPI, UploadFile, File
import shutil
import os
from excel_reader import read_excel
from pdf_reader import extract_pdf_text
from data_mapper import map_data
app = FastAPI()
UPLOAD_FOLDER = "../uploads"
OUTPUT_FOLDER = "../outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
@app.get("/")
def home():
    return {"message": "Excel Bot Running"}
@app.post("/upload-excel")
async def upload_excel(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_FOLDER}/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    data = read_excel(file_path)
    return {"data": data}
@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_FOLDER}/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    text = extract_pdf_text(file_path)
    return {"text": text}
@app.post("/process-excel")
async def process_excel(file: UploadFile = File(...)):
    input_path = f"{UPLOAD_FOLDER}/{file.filename}"
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    output_path = f"{OUTPUT_FOLDER}/processed_{file.filename}"
    map_data(input_path, output_path)
    return {"output_file": output_path}