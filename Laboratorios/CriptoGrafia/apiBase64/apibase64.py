import base64

from modelodatos import ModeloDatos
from fastapi import FastAPI

app: FastAPI = FastAPI(
    title = "TalentoTech Cifrado API, Base 64 ",
    description = "Se va usar Base64 para Cifrado"
)
#cifrar Get
@app.get(
    "/cifrarbase64",
    summary="Base64",
    description="Cifrado en Base64",
    tags=["Base64"]
)
def cifrarbase64(mensaje1):
    return base64.b64encode(mensaje1.encode('utf-8')).decode('utf-8')
#decifrar Get
@app.get(
    "/decifrarbase64",
    summary="DeBase64",
    description="decifrado en Base64",
    tags=["Base64"]
)
def decifrar_base64(codificado1):
    return base64.b64decode(codificado1.encode('utf-8')).decode('utf-8')
#OTRO
@app.post(
    "/cifrarbase64",
    summary="Base65",
    description="Transferencia",
    tags=["Base64"]
)
async def cifrar_base64(textoplano: ModeloDatos):
    textoplano.Texto = cifrar(textoplano.Texto)
    return textoplano

def cifrar(textoplano):
    mensaje_bytes = textoplano.encode('utf-8')
    textocifrado = base64.b64encode(mensaje_bytes)
    return textocifrado.decode ('utf-8')

def decifrar(textocifrado): 
    textoplano_bytes = base64.b64decode(textocifrado)
    return textoplano_bytes.decode()

#Post
@app.post(
    "/decifrarbase64",
    summary="Base 64 decifrar",
    description="Animo animo",
    tags=["Base64"]
)
async def decifrarbase64(textoplano: ModeloDatos):
    textoplano.Texto = decifrar(textoplano.Texto)
    return textoplano