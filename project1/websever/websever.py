#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
# this will be local host IP: 127.0.0.1
HOST, PORT = '', 8888

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
        message = connectionSocket.recv(1024)
  
        filename = message.split()[1]
        f = open(filename[1:])
        # reads the file
        outputdata = f.read() #Fill in start #Fill in end
        f.close() #close file to free resources
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('HTTP/1.1 200 OK\r\n') # hhtp ok messae
        connectionSocket.send("Content-Type: text/html\r\n\r\n")# content type
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
              connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 
