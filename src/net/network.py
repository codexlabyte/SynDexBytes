import socket
import threading

class P2PNetwork:
    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host
        self.port = port
        self.peers = []

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)
        print(f"Server started on {self.host}:{self.port}")
        while True:
            conn, addr = server.accept()
            print(f"Connection from {addr}")
            threading.Thread(target=self.handle_client, args=(conn,)).start()

    def handle_client(self, conn):
        data = conn.recv(1024).decode()
        print(f"Received: {data}")
        conn.close()

# Test the network
if __name__ == "__main__":
    network = P2PNetwork()
    threading.Thread(target=network.start_server).start()
