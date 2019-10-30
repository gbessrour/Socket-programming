import socket

host = socket.gethostname()  # as both code is running on same pc
port = 55071  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

message = input("Please enter a question -> ")  # take input

while message.lower().strip() != "thank you.":
    client_socket.send(message.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response
    print('Received from server: ' + data)  # show in terminal
    message = input("Pleae enter a question -> ")  # again take input

print('You are welcome. Have a nice day!') # final resopnse
client_socket.close()  # close the connection
