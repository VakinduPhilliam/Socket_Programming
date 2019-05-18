# Python Socket Programming.
# Of the various forms of Inter Process Communication (IPC), sockets are by far the most popular. 
# The combination of sockets with INET makes talking to arbitrary machines around the world unbelievably 
# easy.
# The client application (your browser, for example) uses “client” sockets for client-server communication; 
# the web server it’s talking to uses both “server” sockets and “client” sockets. 
# socketserver — A framework for network servers
# Asynchronous Mixins.
# To build asynchronous handlers, use the ThreadingMixIn and ForkingMixIn classes.
# An example for the ThreadingMixIn class:
 
import socket
import threading
import socketserver

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
        self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def client(ip, port, message):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))

if __name__ == "__main__":

    # Port 0 means to select an arbitrary unused port

    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    with server:
        ip, port = server.server_address

        # Start a thread with the server -- that thread will then start one
        # more thread for each request

        server_thread = threading.Thread(target=server.serve_forever)

        # Exit the server thread when the main thread terminates

        server_thread.daemon = True
        server_thread.start()

        print("Server loop running in thread:", server_thread.name)

        client(ip, port, "Hello World 1")
        client(ip, port, "Hello World 2")
        client(ip, port, "Hello World 3")

        server.shutdown()
