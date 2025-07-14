import base58

# ---- Codificar datos a Base58 ----
texto = input("Ingresa el texto que quieres Cifrar =>   ") 
datos_bytes = texto.encode('utf-8')  # Convertimos a bytes

# Codificamos a Base58
codificado = base58.b58encode(datos_bytes)
print("Texto codificado en Base58:", codificado.decode())

# ---- Decodificar de Base58 a texto original ----
# Aquí asumimos que tenemos el string codificado como texto
codificado_str = codificado.decode()

# Lo convertimos de nuevo a bytes y decodificamos
decodificado_bytes = base58.b58decode(codificado_str)
texto_original = decodificado_bytes.decode('utf-8')

print("Texto decodificado:", texto_original)
