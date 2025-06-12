import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def decrypt_file(encrypted_path, key_b64):
    """Descriptografa um arquivo usando AES-256-CBC"""
    
    key = base64.b64decode(key_b64)
    
    
    with open(encrypted_path, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()
    
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    
    decrypted_path = encrypted_path[:-4]  # Remove extensão .enc
    with open(decrypted_path, 'wb') as f:
        f.write(plaintext)
    
    return decrypted_path

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Descriptografa arquivos com AES-256-CBC')
    parser.add_argument('file', help='Caminho do arquivo criptografado (.enc)')
    parser.add_argument('key', help='Chave de descriptografia em Base64')
    args = parser.parse_args()
    
    decrypted_path = decrypt_file(args.file, args.key)
    
    print(f"Arquivo descriptografado salvo em: {decrypted_path}")
    print("Descriptografia concluída com sucesso!")