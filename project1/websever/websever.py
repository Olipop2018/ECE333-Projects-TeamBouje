#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
ERR= b"""\HTTP/1.1 404 NOT FOUND\r\n"""
OK= b"""\HTTP/1.1 200 OK\r\n"""
content= b"""\Content-Type: text/html\r\n\r\n"""
file= b"404S.html"
#Prepare a sever socket
#Fill in start
# this will be local host IP: 127.0.0.1
HOST, PORT = gethostname(), 8888
#info =getaddrinfo(HOST,PORT)
HOST= gethostbyname(HOST)
# prevents waiting for accepting multiple requests
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# bind the sockect and port number
serverSocket.bind((HOST, PORT))
#server starts listening for request, 
#in this case will listen to 5 request before it it stops listening 
serverSocket.listen(5)


#Fill in end
while True:
    print('Ready to serve')
    connectionSocket, addr = serverSocket.accept() #Fill in start #Fill in end
    #Establish the connection

    try:
        # writes the clients request in to message (the file it wants to access)
        message = connectionSocket.recv(4096)
        if (message == b''):
            continue
        filename = message.split()[1]
       # if(message.count(b".js")):
       #f = open(filename[1:],'rb', 4096, encoding="utf8")
        f = open(filename[1:],'rb')
      #  else:
           # f = open(filename[1:])
        # reads the file
        outputdata = f.read() #Fill in start #Fill in end
        f.close() #close file to free resources
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.sendall(OK) # hhtp ok message
        connectionSocket.sendall(content)# content type
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
              connectionSocket.send(outputdata[i])
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        h = open(file)
        eputdata = h.read()
        h.close()
        connectionSocket.sendall(ERR)
        connectionSocket.sendall(content)
        connectionSocket.sendall(eputdata.encode())
        connectionSocket.send("\r\n".encode())
        #
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 
