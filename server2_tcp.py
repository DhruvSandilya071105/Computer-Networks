import socket
import threading

clients = []
server1_addr = ('localhost', 9999)

def broadcast_to_clients(message, sender=None):
    for client in clients[:]:
        try:
            if client != sender:
                client.send(message.encode())
        except:
            clients.remove(client)

def handle_client(conn, addr):
    print(f"Client {addr} connected to TCP Server 2")
    while True:
        try:
            message = conn.recv(1024).decode()
            if not message:
                break
            print(f"TCP Server 2 received: {message}")
            broadcast_to_clients(message, conn)
            forward_to_server1(message)
        except:
            break
    if conn in clients:
        clients.remove(conn)
    conn.close()

def forward_to_server1(message):
    try:
        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s1.connect(('localhost', 9997))
        s1.send(f"[FROM_S2]{message}".encode())
        s1.close()
    except:
        pass

def receive_from_server1():
    s1_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1_listener.bind(('localhost', 9998))
    s1_listener.listen(5)
    print("TCP Server 2 listening for Server 1 on port 9998...")
    while True:
        conn, addr = s1_listener.accept()
        message = conn.recv(1024).decode()
        print(f"TCP Server 2 received from Server 1: {message}")
        broadcast_to_clients(message)
        conn.close()

threading.Thread(target=receive_from_server1, daemon=True).start()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8888))
server.listen(5)
print("TCP Server 2 running on port 8888...")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn, addr)).start()
