# Python Socket Programming.
# Of the various forms of Inter Process Communication (IPC), sockets are by far the most popular. 
# The combination of sockets with INET makes talking to arbitrary machines around the world unbelievably 
# easy.
# The client application (your browser, for example) uses “client” sockets for client-server communication; 
# the web server it’s talking to uses both “server” sockets and “client” sockets. 
# socketserver — A framework for network servers
# Using a Socket
# There are two sets of verbs to use for communication. 
# You can use 'send' and 'recv', or you can transform your client socket into a file-like beast and use 'read' 
# and 'write'. 

class MySocket:
    """demonstration class only
      - coded for clarity, not efficiency
    """

    def __init__(self, sock=None):

        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0

        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])

            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0

        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))

            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)

            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)
