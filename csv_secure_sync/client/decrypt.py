from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def decrypt_file(enc_filename, key):
    backend = default_backend()

    with open(enc_filename, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(decrypted_padded) + unpadder.finalize()

    original_name = enc_filename.replace('.enc', '.decrypted.csv')
    with open(original_name, 'wb') as f:
        f.write(plaintext)

    print(f"File decrypted as '{original_name}'")

if __name__ == "__main__":
    key = b'ThisIsA16ByteKey'
    decrypt_file("../sample_data/sample.csv.enc", key)
