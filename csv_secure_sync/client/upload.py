import requests
import os

def upload_file(filepath):
    if not os.path.exists(filepath):
        print("File does not exist!")
        return

    with open(filepath, "rb") as f:
        response = requests.post(
            "http://localhost:8080/upload",
            headers={"X-Filename": os.path.basename(filepath)},
            data=f.read()
        )
    print(response.text)

if __name__ == "__main__":
    encrypted_file = "../sample_data/sample.csv.enc"
    upload_file(encrypted_file)
