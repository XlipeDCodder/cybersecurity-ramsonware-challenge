import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

def encrypt_file(file_path, key=None):
    """Criptografa um arquivo usando AES-256-CBC"""
    
    key = key or get_random_bytes(32)
    
    
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    
    
    iv = get_random_bytes(16)
    
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    
    
    encrypted_path = file_path + '.enc'
    with open(encrypted_path, 'wb') as f:
        f.write(iv)
        f.write(ciphertext)
    
    
    return base64.b64encode(key).decode('utf-8'), encrypted_path

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Criptografa arquivos com AES-256-CBC')
    parser.add_argument('file', help='Caminho do arquivo a ser criptografado')
    args = parser.parse_args()
    
    key, encrypted_path = encrypt_file(args.file)
    
    print(f"Arquivo criptografado salvo em: {encrypted_path}")
    print(f"CHAVE (guarde com segurança!): {key}")
    print("\nATENÇÃO: Sem esta chave, os dados serão PERDIDOS permanentemente!")