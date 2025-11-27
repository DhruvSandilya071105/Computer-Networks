import socket
import threading

def handle_client(conn, addr):
    print(f"Client {addr} connected")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data or data.lower() == 'exit':
                break
            print(f"Received from {addr}: {data}")
            conn.send(data.encode())
        except:
            break
    conn.close()
    print(f"Client {addr} disconnected")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(5)
print("Echo server running on port 9999...")

while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()
