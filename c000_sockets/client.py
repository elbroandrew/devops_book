import socket


sock = socket.socket(    
    family=socket.AF_INET,
    type=socket.SOCK_STREAM,
    proto=0,
)

sock.bind(("127.0.0.1", 5002))
sock.connect(("127.0.0.1", 5001))
sock.close()

