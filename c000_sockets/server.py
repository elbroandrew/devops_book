import socket

s = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM, # TCP 
    proto=0, # 6 ?

)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # это позволяет опять использовать сокет сразу же после остановки (чтоб не ждать конца тайм айта),
# SO_REUSEPORT - это позволяет двум приложениям(? или сокетам) слушать один порт, и низвестно, куда будет писаться.
# здесь надо четко понимать, что делаю. Не использовать это. Только SO_REUSEADDR.
# 1 - я так понял, это время задержки, если есть какие-то неотправленные данные чтоб успели отправиться?

s.bind(("127.0.0.1", 5001))
s.listen()
client_addr, client_sock = s.accept()
print("Client address: %s, client socket: %s" % (client_addr, client_sock))
s.close()


