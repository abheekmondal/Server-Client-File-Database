File Server and Client

This repository contains two Python programs: server.py and client.py. The server program allows clients to download files hosted on the server, and the client program allows users to download files from the server.

Server
The server.py program starts a file server that listens for incoming client connections on a specified IP address and port. The server hosts a directory of files that clients can download.

To start the server, run the following command:

	python server.py

By default, the server listens on localhost port 8000. You can change the IP address and port by modifying the ip and port variables in the Server class.

When a client connects to the server, the server creates a new thread to handle the client's requests. The thread waits for a command from the client and then executes the corresponding action. The server supports two commands:

get_files_list: The server sends a JSON-encoded dictionary to the client containing the names and sizes of all the files in the server's file directory.
download filename: The server sends the contents of the specified file to the client. If the file does not exist on the server, the server sends an error message to the client.
the server_databases folder contains all the files that the client can download.

Client
The client.py program allows users to download files from the server. The client can connect to a remote server or a local server running on the same machine.

To start the client, run the following command:

	python client.py

By default, the client connects to localhost port 8000. You can change the IP address and port by using command line arguments:

	python client.py --ip <ip_address> --port <port_number>

The client program supports the following features:

Get file list: The client sends a request to the server for a list of all the files in the server's file directory. The server responds with a JSON-encoded dictionary containing the names and sizes of all the files.
Download file(s): The client can download one or more files from the server. The user enters the names of the files to download, and the client program downloads each file in sequence. The client can download files in parallel by using the --parallel command line argument. By default, files are downloaded sequentially.
Exit: The client program can be terminated by entering the command 3.
By default, downloaded files are saved in a directory called client_env in the current working directory. You can change the directory by using the --save-dir command line argument:

	python client.py --save-dir <directory_path>


Subprocess Program
Additionally, there is a program called subprocess_program.py that demonstrates how to use the subprocess module to run shell commands from within a Python program. This program runs a shell command to list the contents of the current directory and then prints the output to the console. you can change the number of threads in the program by changing the n value. All threads will randomly choose a file within the files array, but the threads will all download the same file. 
You can check the elapsed time for all the threads in the total_download_time.txt file.


Installation:

1. Clone this repository to your local machine.
2. Make sure you have Python 3.x installed on your machine.
3. Install the requests library by running pip install requests in your command prompt or terminal.
NOTE: There are no additional libraries that need to be installed

Running the program
To run the program, first start the server by running the following command in a terminal window:

	python server.py

This will start the server on localhost at port 8000. To change the IP address and port number, modify the ip and port parameters of the Server constructor in server.py.
To run the client, open another terminal window and run the following command:

	python client.py

This will start the client in interactive mode. The client has a menu that allows the user to get a list of files hosted by the server and download one or more files.
The --save-dir command-line option can be used to specify the directory where downloaded files will be saved. By default, downloaded files will be saved in the client_env directory in the same directory as client.py.
The --ip and --port command-line options can be used to specify the IP address and port number of the server.

Client program commands
The client program has the following commands:

1: Get list of files hosted by the server
2: Download file(s) from the server
3: Exit the program
When 1 is entered, the client will get a list of files hosted by the server and print them to the console.

When 2 is entered, the client will prompt the user to enter one or more filenames to download, separated by commas. The files will be downloaded one at a time and their checksums will be printed to the console. The total download time will also be printed to the console.

When 3 is entered, the client program will exit.

Subprocess_Test Program Commands
Start the server, run the following command to start the tests:

	python subprocess_test.py

For specific tests:
1. Open Open subprocess_test.py in your preferred text editor.
2. In the files array, add the URLs of the files, from the server database, you wish to download.
3. You can change the number of threads in the program by changing the value of n in the subprocess_test.py file.
4. The threads will randomly choose a file within the files array to download. However, all threads will download the same file.
5. Once the download is complete, the elapsed time for all the threads will be written to total_download_time.txt.