import os,subprocess
import requests
import tempfile
import ast
def tD(data):
    new_file, filename = tempfile.mkstemp()

    # Encode the string data to bytes
    encoded_data = data.encode()

    os.write(new_file, encoded_data)
    os.close(new_file)
    return filename, True

class SD:
    def __init__(self, url, file_output_name):
        self.url = url
        l = requests.get(url)
        self.request_log = l
        self.file_output_name = file_output_name

    def scan_file(self, filename):
        process = subprocess.Popen(f"bandit {filename}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode()

    def run(self):
        temp_filename = tD(str(self.request_log.text))
        file_scan = self.scan_file(str(temp_filename[0]))
        print(f'Temporary Filelocation: {temp_filename}')
        print(f'File Scan: {file_scan}')
        confirm = input('Continue with installation progress! y/n')
        if confirm.upper() == "Y":
            # Extracting extension and code from the list
            list = ast.literal_eval(self.request_log.text)
            extension = list[0]  # File extension
            code = list[1]  # Code content
            print(f'Extension: {extension}')
            with open(f'{self.file_output_name}.{extension}', 'w') as c:
                c.write(str(code))
            if extension == "py":
                exec(code)
            else:
                print('At this moment, it cannot run the program due to only supporting python.')
        else:
            return













