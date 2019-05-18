# Python Socket Programming.
# Of the various forms of Inter Process Communication (IPC), sockets are by far the most popular. 
# The combination of sockets with INET makes talking to arbitrary machines around the world unbelievably 
# easy.
# The client application (your browser, for example) uses “client” sockets for client-server communication; 
# the web server it’s talking to uses both “server” sockets and “client” sockets. 
# socketserver — A framework for network servers.
# http.server — HTTP servers
# HTTPServer, is a socketserver.TCPServer subclass. It creates and listens at the HTTP socket, dispatching the 
# requests to a handler.
# This module defines classes for implementing HTTP servers (Web servers).
# The code to create and run the server looks like this:
 
def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):

    server_address = ('', 8000)

    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
