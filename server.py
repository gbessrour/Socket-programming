import socket

host = socket.gethostname() # get the hostname
port = 55011  # initiate port no above 1024

server_socket = socket.socket()  # get instance

server_socket.bind((host, port))  # bind host address and port together

server_socket.listen(2) # configure how many client the server can listen simultaneously

conn, address = server_socket.accept()  # accept new connection
print("Connection from: " + str(address))
while True:
   # receive data stream. it won't accept data packet greater than 1024 bytes
    data = conn.recv(1024).decode()  
    
    if not data:
    # if data is not received break
        break

    # If statement blocks for questions and answers.
    if data.lower() == "what is your name?":
        data = "My name is Ghassen Bessrour."

    elif data.lower() == "how many programming assignments do we have?":
        data = "I think there are two."

    elif data.lower() == "do you think the second part is more challenging?":
        data = "Of course, the first part (socket programming) has been done for you."

    elif data.lower() == "how do you know to respond to these questions?":
        data = "You programmed me, didn’t you?"

    elif data.lower() == "can i ask you a personal question?":
        data = "I don’t think you’d like the answer."

    elif data.lower() == "can you answer an arbitrary question?":
        data = "Yes, I can, but I won’t."        

    else:
        data = "I do not understand your question. Please re-enter your question."

    conn.send(data.encode())  # send data to the client

conn.close()  # close the connection