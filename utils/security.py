import base64

# Para encriptar contraseñas
def encrypt(text: str):
  # Condifica el texto en base64
  encoded_bytes = base64.b64encode(text.encode('utf-8'))

  # Convierte los bytes de nuevo en una cadena
  encrypted_text = encoded_bytes.decode('utf-8')

  return encrypted_text

# Para desencriptar contraseñas
def decrypt(encrypted_text: str):
  # Decodificar el texto codificado en base64 a bytes
  decoded_bytes = base64.b64decode(encrypted_text.encode('utf-8'))
  
  # Convierte los bytes de nuevo en una cadena
  decrypted_text = decoded_bytes.decode('utf-8')

  return decrypted_text