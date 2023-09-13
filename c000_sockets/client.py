import socket


sock = socket.socket(    
    family=socket.AF_INET,
    type=socket.SOCK_STREAM,
    proto=0,
)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.connect(("127.0.0.1", 5001))
sock.close()

