#!/usr/bin/env python3
import socket
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

addr_info = socket.getaddrinfo("www.google.com", 80, proto=socket.SOL_TCP)
(family, socketype, proto, canonname, sockaddr) = addr_info[0]

def getResponse(sock):
    full_data = b""
    while True:
        data = sock.recv(BUFFER_SIZE)
        if data:
            full_data += data
        else:
            break
    return full_data

def handle_proxy(conn, addr):
    with conn:
        with socket.socket(family, socketype) as proxy_dest:
            proxy_dest.connect(sockaddr)

            full_data = getResponse(conn)
            #print(full_data)
            proxy_dest.sendall(full_data)
            response = getResponse(proxy_dest)
            #print(response)
            conn.sendall(response)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((HOST, PORT))
        sock.listen(1)

        while True:
            conn, addr = sock.accept()
            p = Process(target=handle_proxy, args=(conn, addr))
            p.daemon = True
            p.start()

if __name__ == "__main__":
    main()