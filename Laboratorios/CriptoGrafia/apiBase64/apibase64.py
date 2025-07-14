import base64

from fastapi import FastAPI

app: FastAPI = FastAPI(
    title = "TalentoTech Cifrado API, Base 64 ",
    description = "Se va usar Base64 para Cifrado"
)

@app.get(
    "/cifrarbase64",
    summary="Base64",
    description="Cifrado en Base64",
    tags=["Base64"]
)
def cifrarbase64(mensaje1):
    return base64.b64encode(mensaje1.encode('utf-8')).decode('utf-8')

@app.get(
    "/decifrarbase64",
    summary="DeBase64",
    description="decifrado en Base64",
    tags=["Base64"]
)

def decifrar_base64(codificado1):
    return base64.b64decode(codificado1.encode('utf-8')).decode('utf-8')


