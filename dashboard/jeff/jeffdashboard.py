import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9490))


while True:
    msg = s.recv(1024)
    if msg:
        print("Données telemetriques ==========> ", end='')
        print(msg.decode("utf-8"))