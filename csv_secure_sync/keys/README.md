# CSV Secure Sync - Client

This folder includes Python scripts for securely encrypting, decrypting, and uploading CSV files.

## Files

- `encrypt.py`: Encrypts a CSV file using AES CBC mode
- `decrypt.py`: Decrypts an encrypted `.enc` file back to readable CSV
- `upload.py`: Sends the encrypted file to the Flask server over HTTP
- `README.md`: You are reading it!

## Key Setup

We use a static key (`ThisIsA16ByteKey`) for demo purposes. Replace it with a securely generated key in real use.

## How to Run

```bash
# Activate your Python environment
python encrypt.py        # Encrypt the CSV
python decrypt.py        # Decrypt it (for testing)
python upload.py         # Upload encrypted file to server
