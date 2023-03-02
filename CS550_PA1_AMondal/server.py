import socket
import os
import json
import hashlib
import threading

class ClientThread(threading.Thread):
    def __init__(self, client_socket, client_address, file_directory):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.client_address = client_address
        self.file_directory = file_directory

    def run(self):
        while True:
            data = self.client_socket.recv(1024).decode()
            if not data:
                break

            tokens = data.split()
            command = tokens[0]
            if command == 'get_files_list':
                file_list = self.get_file_list()
                self.client_socket.sendall(json.dumps(file_list).encode())
            elif command == 'download':
                filename = tokens[1]
                file_path = os.path.join(self.file_directory, filename)
                if not os.path.isfile(file_path):
                    self.client_socket.sendall(f'File {filename} not found on server.'.encode())
                else:
                    with open(file_path, 'rb') as f:
                        data = f.read()
                    self.client_socket.sendall(data)

        self.client_socket.close()

    def get_file_list(self):
        files = os.listdir(self.file_directory)
        file_list = {}
        for filename in files:
            file_path = os.path.join(self.file_directory, filename)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                file_list[filename] = file_size
        return file_list


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.file_directory = 'server_database'

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.ip, self.port))
        server_socket.listen(5)
        print(f'Server listening on {self.ip}:{self.port}...')

        while True:
            client_socket, client_address = server_socket.accept()
            print(f'Accepted connection from {client_address[0]}:{client_address[1]}')
            client_thread = ClientThread(client_socket, client_address, self.file_directory)
            client_thread.start()


if __name__ == '__main__':
    server = Server('localhost', 8000)
    server.start()
