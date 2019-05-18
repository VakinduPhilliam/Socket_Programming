# Python Socket Programming.
# Of the various forms of Inter Process Communication (IPC), sockets are by far the most popular. 
# The combination of sockets with INET makes talking to arbitrary machines around the world unbelievably 
# easy.
# The client application (your browser, for example) uses “client” sockets for client-server communication; 
# the web server it’s talking to uses both “server” sockets and “client” sockets. 
# socketserver — A framework for network servers
# An alternative socketserver request handler class that makes use of streams (file-like objects that simplify 
# communication by providing the standard file interface):
 
class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):

        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls

        self.data = self.rfile.readline().strip()

        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

        # Likewise, self.wfile is a file-like object used to write back
        # to the client

        self.wfile.write(self.data.upper())
