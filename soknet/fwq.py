'''
2018.8.30
'''
import socket

HOST = '172.25.11.187'
PORT = 55555

with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

