from PIL import Image
import pytesseract
import os

def validate_document(filename: str) -> str:
    try:
        filepath = os.path.join("sample_docs", filename)
        image = Image.open(filepath)
        text = pytesseract.image_to_string(image)

        if "CPF" in text or "Nome" in text:
            return f"Documento válido: Texto identificado: {text[:100]}..."
        return "Texto não reconhecido como válido."
    except Exception as e:
        return f"Erro ao processar documento: {str(e)}"

def analyze_social_link(link: str) -> dict:
    return {
        "platform": "Twitter" if "twitter" in link else "Desconhecida",
        "related_to_esports": "FURIA" in link.upper(),
        "activity_summary": "Usuário segue várias organizações de eSports."
    }
