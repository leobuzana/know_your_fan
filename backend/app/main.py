from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
from utils.ai_validation import validate_document
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Supabase client
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Endpoint para upload de documentos
@app.post("/upload-doc/")
async def upload_document(file: UploadFile = File(...)):
    contents = await file.read()
    file_path = f"sample_docs/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(contents)

    # Validação com OCR
    result = validate_document(file.filename)

    # Aqui você pode adicionar o usuário no Supabase se necessário
    # Exemplo: inserir dados do documento

    return {"filename": file.filename, "result": result}

@app.get("/user/{user_id}")
async def get_user(user_id: str):
    user = supabase.from("users").select("*").eq("id", user_id).execute()
    return JSONResponse(content=user.data)
