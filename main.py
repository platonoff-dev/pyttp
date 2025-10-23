import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8080))
    sock.listen()
    
    while True:
        conn, _ = sock.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                conn.send(f"receied {data}".encode())


if __name__ == "__main__":
    main()
