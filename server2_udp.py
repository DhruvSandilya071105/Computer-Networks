import socket
import threading

clients = set()
server1_addr = ('localhost', 9999)

def handle_messages():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('localhost', 8888))
    print("UDP Server 2 running on port 8888...")

    while True:
        message, addr = server.recvfrom(1024)
        message = message.decode()
        clients.add(addr)
        print(f"UDP Server 2 received: {message} from {addr}")

        # Broadcast to all clients except sender
        for client_addr in clients:
            if client_addr != addr:
                try:
                    server.sendto(message.encode(), client_addr)
                except:
                    pass

        # Forward to Server 1
        try:
            s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s1.sendto(f"[FROM_S2]{message}".encode(), server1_addr)
        except:
            pass

threading.Thread(target=handle_messages).start()
