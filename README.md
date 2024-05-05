# Computer Networks CSE310 Assignment 1
<ins>proxyserver.py:

The following code mplements a simple web proxy server with caching functionality. It intercepts HTTP requests from clients, forwards them to the appropriate server, caches responses, and serves cached responses if available.

createRequest Function: This function creates an HTTP request header based on the provided host, URL, and original request. It extracts necessary information from the original request such as user-agent, accept, referer, etc.

createResponse Function: This function creates an HTTP response header based on the filename and the data received. It determines the content type based on the file extension and sets the content length accordingly.

create404 Function: This function creates a 404 Not Found response header.

BUFFER_SIZE and welcomePort: Definitions of buffer size and port number.

welcomeSocket: It creates a welcoming socket, binds it to the specified server IP and port, and starts listening for incoming connections.

Listening Loop: It continuously listens for incoming connections.

Parsing Request: It receives requests from clients, parses the request headers to extract the method, URL, and host.

Caching Mechanism: If the requested file is found in the cache (i.e., the local directory), it serves the file directly to the client. Otherwise, it forwards the request to the original server, receives the response, caches the response, and then sends it back to the client.

Error Handling: It handles various exceptions such as timeouts, file not found, and general exceptions.

Keyboard Interrupt Handling: It handles keyboard interrupt gracefully.

<ins>webserver.py:

This code essentially implements a basic HTTP server that can serve static files from the file system.

Socket Creation and Binding: It creates a TCP socket (SOCK_STREAM) and binds it to the specified server IP address (input by the user) and port (6789).

Listening for Connections: It listens for incoming connections with a maximum queue size of 1.

Connection Handling Loop: It continuously waits for incoming connections.

Receiving and Parsing Request: When a connection is accepted, it receives the HTTP request message from the client, parses the filename from the request, and opens the corresponding file.

Handling File: If the requested file exists, it reads the file contents and sends an HTTP 200 OK response along with the file contents to the client.

Error Handling: If the requested file does not exist (IOError), it sends an HTTP 404 Not Found response to the client.

Closing Connection: After handling the request, it closes the connection.

Closing Server Socket: It closes the server socket after the loop.
