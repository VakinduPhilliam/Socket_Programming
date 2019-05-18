# Python Socket Programming.
# Of the various forms of Inter Process Communication (IPC), sockets are by far the most popular. 
# The combination of sockets with INET makes talking to arbitrary machines around the world unbelievably 
# easy.
# The client application (your browser, for example) uses “client” sockets for client-server communication; 
# the web server it’s talking to uses both “server” sockets and “client” sockets. 
# socketserver — A framework for network servers
# class socketserver.StreamRequestHandler class socketserver.DatagramRequestHandler
# These BaseRequestHandler subclasses override the setup() and finish() methods, and provide self.rfile and 
# self.wfile attributes. 
# The self.rfile and self.wfile attributes can be read or written, respectively, to get the request data or
# return data to the client.
# The rfile attributes of both classes support the io.BufferedIOBase readable interface, and DatagramRequestHandler.wfile 
# supports the io.BufferedIOBase writable interface.
# This is the server side:
 
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):

        # self.request is the TCP socket connected to the client

        self.data = self.request.recv(1024).strip()

        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

        # just send back the same data, but upper-cased

        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:

        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C

        server.serve_forever()
