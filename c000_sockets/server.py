import socket

s = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM, # TCP 
    proto=0, # 6 ?

)

s.bind("127.0.0.1", 5001)
s.listen()
client_addr, client_sock = s.accept()
print("Client address: %s, client socket: %s" % client_addr, client_sock)
s.close()


