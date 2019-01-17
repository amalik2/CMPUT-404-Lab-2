#!/usr/bin/env python3
import socket
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def handle_echo(conn, addr):
    with conn:
        print(conn)
        print(addr)
        full_data = b""
        while True:
            data = conn.recv(BUFFER_SIZE)
            if data:
                full_data += data
            else:
                break
        print(full_data)
        conn.sendall(full_data)
        conn.shutdown(socket.SHUT_RDWR)
        print(conn.recv(BUFFER_SIZE))

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((HOST, PORT))
        sock.listen(1)

        while True:
            conn, addr = sock.accept()
            p = Process(target=handle_echo, args=(conn, addr))
            p.daemon = True
            p.start()

if __name__ == "__main__":
    main()