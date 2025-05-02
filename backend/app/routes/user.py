@router.post("/upload-doc")
async def upload_doc(file: UploadFile = File(...)):
    contents = await file.read()
    filepath = f"sample_docs/{file.filename}"
    with open(filepath, "wb") as f:
        f.write(contents)

    result = ai_validation.validate_document(file.filename)
    return {"filename": file.filename, "validation_result": result}
