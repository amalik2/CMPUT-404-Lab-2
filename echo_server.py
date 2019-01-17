#!/usr/bin/env python3
import socket

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((HOST, PORT))
        sock.listen(1)

        while True:
            conn, addr = sock.accept()
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
            print(conn.recv(BUFFER_SIZE))

if __name__ == "__main__":
    main()