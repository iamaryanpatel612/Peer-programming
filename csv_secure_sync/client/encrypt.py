from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def encrypt_file(filename, key):
    backend = default_backend()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()

    with open(filename, 'rb') as f:
        plaintext = f.read()

    padder = padding.PKCS7(128).padder()
    padded = padder.update(plaintext) + padder.finalize()
    ciphertext = encryptor.update(padded) + encryptor.finalize()

    with open(filename + '.enc', 'wb') as f:
        f.write(iv + ciphertext)

    print(f"File '{filename}' encrypted as '{filename}.enc'")

if __name__ == "__main__":
    key = b'ThisIsA16ByteKey'  # Must be 16, 24, or 32 bytes
    filename = "../sample_data/sample.csv"
    encrypt_file(filename, key)
