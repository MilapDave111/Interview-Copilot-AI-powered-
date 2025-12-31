import os

os.environ["PATH"] += os.pathsep + r"C:\ffmpeg-2025-12-28-git-9ab2a437a1-full_build\bin"

from fastapi import FastAPI,UploadFile,File
import shutil
import whisper
import traceback

app = FastAPI()

print("Loading Whisper AI Model... (This might take a moment) ")
model = whisper.load_model("base")
print("Model Loaded!")

@app.get("/")
def read_root():
    return {"message": "Hello from Python AI Service! I am ready."}

@app.post("/transcribe")
async def transcribe_audio(file:UploadFile=File(...)):
    temp_filename= f"temp_{file.filename}"

    with open(temp_filename,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    result = model.transcribe(temp_filename)

    return {"transcript" : result["text"]}

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        # 1. Save temp file
        temp_filename = f"temp_{file.filename}"
        with open(temp_filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        print(f"File saved to {temp_filename}. Starting Whisper...")

        # 2. Transcribe
        result = model.transcribe(temp_filename)
        
        print("Transcription success!")
        return {"transcript": result["text"]}

    except Exception as e:
        # <--- THIS WILL PRINT THE REAL ERROR TO YOUR TERMINAL
        print(f"CRITICAL ERROR: {str(e)}")
        traceback.print_exc() 
        return {"error": str(e)}