#!/usr/bin/env python3
import socket

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = """GET / HTTP/1.0
Host: www.google.com

"""

def connect_socket(addr):
    (family, socketype, proto, cannonName, sockaddr) = addr
    try:
        sock = socket.socket(family, socketype, proto)
        sock.connect(sockaddr)
        sock.sendall(payload.encode())
        sock.shutdown(socket.SHUT_WR)
        full_data = b""
        while True:
            data = sock.recv(BUFFER_SIZE)
            if data:
                full_data += data
            else:
                break
        print(full_data)
    except:
        print("Not connected")
    finally:
        sock.close()

def main():
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
    addr = addr_info[0]
    connect_socket(addr)
    
    print("-")

if __name__ == "__main__":
    main()