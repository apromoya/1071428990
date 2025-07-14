import base64

def codificar_base64(mensaje1):
    return base64.b64encode(mensaje1.encode('utf-8')).decode('utf-8')

def decodificar_base64(codificado1):
    return base64.b64decode(codificado1.encode('utf-8')).decode('utf-8')

# Ejemplo de uso
if __name__ == "__main__":
    texto = input("Ingresa el Mensaje a Cifrar ==>  ")
    codificado = codificar_base64(texto)
    decodificado = decodificar_base64(codificado)

    print("\n---- Resultados ----")
    print("Codificado:", codificado)
    print("Decodificado:", decodificado)
