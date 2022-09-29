from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
text = input("Enter your ip address")
serverSocket.bind((text, serverPort))
serverSocket.listen(1)
while True:
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        print ('Message is: ', message)
        filename = message.split()[1]
        print ('File name is: ', filename)
        f = open(filename[1:])
        outputdata = f.read()
        print("Output data is: ", outputdata)
        connectionSocket.send(bytes("HTTP/1.1 200 OK\n","UTF-8"))
        connectionSocket.send(bytes("Content-Type: text/html\n", "Utf-8"))
        connectionSocket.send(bytes("\n","UTF-8"))
        connectionSocket.send(outputdata.encode())
        # for i in range(0, len(outputdata)):
        #     connectionSocket.send(outputdata[i].encode())
        connectionSocket.send(bytes("\r\n", "UTF-8"))
        delete = input()
        connectionSocket.close()
    except IOError:
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\n","UTF-8"))
        connectionSocket.send(bytes("Content-Type: text/html\n", "Utf-8"))
        connectionSocket.send(bytes("\n","UTF-8"))
        connectionSocket.send(bytes("<head><body>404 Not Found</head></body>\r\n","UTF-8"))
connectionSocket.close()
serverSocket.close()