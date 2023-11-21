from base64 import b64encode, b64decode
from cryptography.fernet import Fernet
import base64
import os

def encode(phone, action):
      # mi_clave_bytes = b'DiriTelecomunicacionesSAdeCV'  # Ejemplo, reemplaza con tu clave
      
      mi_clave_bytes = os.urandom(32)
      # Codifica la clave en base64
      mi_clave_base64 = base64.urlsafe_b64encode(mi_clave_bytes)
  
      secret_key=Fernet(mi_clave_base64)    
      
      if action == 'e':
        encrypt_data = secret_key.encrypt(phone.encode())
        return b64encode(encrypt_data).decode('utf-8')
    
      elif action == 'd':
          decrypt_data = secret_key.decrypt(phone).decode()
          return decrypt_data.decode('utf-8')

def encodee(phone, action):
    # Generar una clave aleatoria de 32 bytes
    clave_bytes = os.urandom(32)
    # print(clave_bytes)
    # Codificar la clave en base64 de forma segura
    clave_base64 = base64.urlsafe_b64encode(b"\x1ejT\x80\x19z\xf2\x9c\x94\xb4(\x90\xeb;\x12\xd3\x1b\x94H\xe7\xf0\xa0$\x9d\xb9e\xdd;\xa1\x1c\x8a^" )

    # Crear un objeto Fernet con la clave codificada en base64
    secret_key = Fernet(clave_base64)

    if action == 'e':
        encrypt_data = secret_key.encrypt(phone.encode())
        return base64.urlsafe_b64encode(encrypt_data).decode('utf-8')

    elif action == 'd':
        decrypt_data = secret_key.decrypt(base64.urlsafe_b64decode(phone)).decode('utf-8')
        return decrypt_data

print('Codificado')
print(encodee('5628517184', 'e'))
print('Decodificado')
print(encodee('Z0FBQUFBQmxMWVFwa2JTT0g3T2NUeUtuTXg4Y1dqbjlhb3l0eF9pTUl1V09nM3VzUjd2b1FTblNHdDRpd09sTmdGZllrWnlYUmdZNUVEdTZ3MWMyYXUza3NQaWREdUlGYUE9PQ==', 'd'))