# Python FastAPI File Upload Server

This repository contains a simple Python FastAPI server for handling file uploads. The server allows users to upload files, which are then saved to a specified directory on the server.

## File Structure
```
src/
├── upload_file.py # Python FastAPI server for file uploads
```

## Features

- Upload single or multiple files.
- Save uploaded files to a designated directory.
- Simple and lightweight FastAPI implementation.

## Prerequisites

Before running the server, ensure you have the following installed:

- Python 3.8 or higher
- FastAPI (`pip install fastapi`)
- Uvicorn (`pip install uvicorn`)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/architattrey/python-fastAPI.git
   cd python-fastAPI
    ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   uvicorn upload_file:app --reload
   ```
4. Open your browser and navigate to http://127.0.0.1:8000 to access the server.

## Usage

### Uploading Files

1. Use the /upload endpoint to upload files:

   - **Single File Upload**: Send a POST request to /upload with a file attached.
   - **Multiple Files Upload**: Send a POST request to /upload with multiple files attached.

2. Example using **curl**:
   ```
   curl -X POST -F "file=@/path/to/your/file.txt" http://127.0.0.1:8000/upload
   ```
3. Example using Python **requests**:
   ```
    import requests
    url = "http://127.0.0.1:8000/upload"
    files = {"file": open("path/to/your/file.txt", "rb")}
    response = requests.post(url, files=files)
    print(response.json())
   ```
## API Endpoints
### **POST /upload**: Upload one or more files.

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

## License
This project is licensed under the[MIT licensed](LICENSE). See the LICENSE file for details.

## Link to upload_file.py
You can view the main server file here: upload_file.py
