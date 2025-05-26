from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploaded/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    filename = request.headers.get('X-Filename', 'uploaded_file.csv.enc')
    file_data = request.get_data()
    with open(os.path.join(UPLOAD_FOLDER, filename), 'wb') as f:
        f.write(file_data)
    return "File uploaded and saved.\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
