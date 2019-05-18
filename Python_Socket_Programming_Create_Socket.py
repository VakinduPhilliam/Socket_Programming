# Python Socket Programming.
# Of the various forms of Inter Process Communication (IPC), sockets are by far the most popular. 
# The combination of sockets with INET makes talking to arbitrary machines around the world unbelievably 
# easy.
# The client application (your browser, for example) uses “client” sockets for client-server communication; 
# the web server it’s talking to uses both “server” sockets and “client” sockets. 
# socketserver — A framework for network servers
# Creating a Socket.

# Client Side
# When you click on a web link, your browser does something like the following:
 
# create an INET, STREAMing socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# now connect to the web server on port 80 - the normal http port

s.connect(("www.python.org", 80))

# Server Side.
# What happens in the web server is a bit more complex. First, the web server creates a “server socket”:
 
# create an INET, STREAMing socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a public host, and a well-known port

serversocket.bind((socket.gethostname(), 80))

# become a server socket

serversocket.listen(5)
