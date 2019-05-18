# Python Socket Programming.
# Of the various forms of Inter Process Communication (IPC), sockets are by far the most popular. 
# The combination of sockets with INET makes talking to arbitrary machines around the world unbelievably 
# easy.
# The client application (your browser, for example) uses “client” sockets for client-server communication; 
# the web server it’s talking to uses both “server” sockets and “client” sockets. 
# socketserver — A framework for network servers
# socketserver.UDPServer
# Server side:
 
import socketserver

class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):

        data = self.request[0].strip()
        socket = self.request[1]

        print("{} wrote:".format(self.client_address[0]))
        print(data)

        socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()
