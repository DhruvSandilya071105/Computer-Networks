import socket
import threading

clients = []
server2_addr = ('localhost', 8888)

def broadcast_to_clients(message, sender=None):
    for client in clients[:]:
        try:
            if client != sender:
                client.send(message.encode())
        except:
            clients.remove(client)

def handle_client(conn, addr):
    print(f"Client {addr} connected to Server 1")
    while True:
        try:
            message = conn.recv(1024).decode()
            if not message:
                break
            print(f"Server 1 received: {message}")
            broadcast_to_clients(message, conn)
            # Forward to Server 2
            forward_to_server2(message)
        except:
            break
    if conn in clients:
        clients.remove(conn)
    conn.close()

def forward_to_server2(message):
    try:
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s2.connect(('localhost', 9998))
        s2.send(f"[FROM_S1]{message}".encode())
        s2.close()
    except:
        pass

def receive_from_server2():
    s2_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2_listener.bind(('localhost', 9997))
    s2_listener.listen(5)
    print("Server 1 listening for Server 2 on port 9997...")
    while True:
        conn, addr = s2_listener.accept()
        message = conn.recv(1024).decode()
        print(f"Server 1 received from Server 2: {message}")
        broadcast_to_clients(message)
        conn.close()

# Start inter-server listener
threading.Thread(target=receive_from_server2, daemon=True).start()

# Main server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(5)
print("Server 1 running on port 9999...")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn, addr)).start()
