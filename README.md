# Computer Networks CSE310 Assignment 1
proxyserver.py:

The following code mplements a simple web proxy server with caching functionality. It intercepts HTTP requests from clients, forwards them to the appropriate server, caches responses, and serves cached responses if available.

webserver.py:

This code essentially implements a basic HTTP server that can serve static files from the file system.
Socket Creation and Binding: It creates a TCP socket (SOCK_STREAM) and binds it to the specified server IP address (input by the user) and port (6789).
Listening for Connections: It listens for incoming connections with a maximum queue size of 1.
Connection Handling Loop: It continuously waits for incoming connections.
Receiving and Parsing Request: When a connection is accepted, it receives the HTTP request message from the client, parses the filename from the request, and opens the corresponding file.
Handling File: If the requested file exists, it reads the file contents and sends an HTTP 200 OK response along with the file contents to the client.
Error Handling: If the requested file does not exist (IOError), it sends an HTTP 404 Not Found response to the client.
Closing Connection: After handling the request, it closes the connection.
Closing Server Socket: It closes the server socket after the loop.
