import os
import socket

from format import Request

PORT = int(os.getenv("LISTEN_PORT", "8080"))

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', PORT))
    sock.listen()
    print(f"Listen on port :{PORT}")
    
    while True:
        conn, addr = sock.accept()
        print(f"Accept connection: {addr}")
        conn_data = bytes()
        with conn:
            while True:
                print("Receiving data")
                data = conn.recv(1024 * 1024)
                conn_data += data
                if not data:
                    conn.send(b"received")
                    break
                
        try:
            req = Request.parse(conn_data)
            print(f"Got request: {req}")
        except Exception as e:
            print(f"Failed to parse request: {e}")
            
if __name__ == "__main__":
    main()
