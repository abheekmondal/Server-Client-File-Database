import socket
import hashlib
import json
import os
import time
import argparse

class Client:
    def __init__(self, ip, port, save_dir):
        self.ip = ip
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.ip, self.port))
        self.save_dir = save_dir

    def get_file_list(self):
        self.client_socket.sendall('get_files_list'.encode())
        data = self.client_socket.recv(1024).decode()
        return json.loads(data)

    def download_file(self, filename):
        self.client_socket.sendall(f"download {filename}".encode())
        data = self.client_socket.recv(1024)
        if isinstance(data, bytes):
            save_path = os.path.join(self.save_dir, filename)
            with open(save_path, 'wb') as f:
                f.write(data)
            checksum = hashlib.md5(data).hexdigest()
            return checksum
        else:
            return str(data)

    def download_files(self, filenames, parallel=False):
        start_time = time.time()
        for filename in filenames:
            checksum = self.download_file(filename)
            print(f'Downloaded {filename} ({os.path.getsize(os.path.join(self.save_dir, filename))} bytes). Checksum: {checksum}')
        '''''''''''''''
            if isinstance(checksum, str):
                print(f'Error downloading {filename}: {checksum}')
            else:
                print(f'Downloaded {filename} ({os.path.getsize(os.path.join(self.save_dir, filename))} bytes). Checksum: {checksum}')
        '''''''''''''''
        end_time = time.time()
        total_time = end_time - start_time
        print(f'Total download time: {total_time} seconds')

    def start(self):
        while True:
            print('\nMenu:')
            print('1. Get file list')
            print('2. Download file(s)')
            print('3. Exit')
            choice = input('Enter your choice: ')

            if choice == '1':
                print('Getting list of files from server...')
                files = self.get_file_list()
                print('List of files hosted by the server:')
                for file_name, file_size in files.items():
                    print(f'{file_name} ({file_size} bytes)')

            elif choice == '2':
                filenames = input('Enter name(s) of file(s) to download (comma-separated): ').split(',')
                filenames = [filename.strip() for filename in filenames]
                if not filenames:
                    print('No files specified')
                    continue
                print('Downloading files from server...')
                self.download_files(filenames)

            elif choice == '3':
                break

            else:
                print('Invalid choice')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Client for file server')
    parser.add_argument('--save-dir', type=str, default='client_env', help='directory to save files')
    parser.add_argument('--ip', type=str, default='localhost', help='server IP address')
    parser.add_argument('--port', type=int, default=8000, help='server port')
    args = parser.parse_args()
    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)
    client = Client(args.ip, args.port, args.save_dir)
    client.start()
