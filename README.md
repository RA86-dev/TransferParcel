# TransferParcel

TransferParcel is a lightweight Python script delivery system designed to fetch Python scripts from a specified URL, perform security scans, and execute them if deemed safe. It serves as a simple Content Delivery Network (CDN) for Python scripts.

## Features

- Fetch Python scripts from a provided URL.
- Scan fetched scripts for security vulnerabilities using Bandit.
- Execute fetched scripts safely if approved by the user.
- Provides basic security measures to mitigate risks associated with executing remote code.

## How It Works

TransferParcel consists of two main components:

1. **SD (Script Delivery) Class**: This class fetches the content from the provided URL using the `requests` library, scans it for security issues using the Bandit tool, and executes it if deemed safe.

2. **tD Function (Temporary Data)**: This function creates a temporary file to store the fetched data securely.

## Usage

To use TransferParcel, follow these steps:

1. Initialize an instance of the `SD` class with the URL of the Python script and the desired output filename.
2. Run the `run` method to fetch, scan, and execute the script.
3. Find a URL from the web. Recommended to first test it with the local script we have along with others.

## Create a CDN for it

You need to provide the Python script content in the following format:
['EXTENSION', 'CODE']

kotlin
Copy code
The reason for this format is to specify the file extension for proper handling.

Example:

```python
from TransferParcel import SD

url = "https://example.com/myscript.py"
output_filename = "myscript"

parcel = SD(url, output_filename)
parcel.run()
```
Replace "https://example.com/myscript.py" with the URL of the Python script you want to fetch, and "myscript" with the desired output filename.

