import socket
import threading

clients = set()
server2_addr = ('localhost', 8888)

def handle_messages():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('localhost', 9999))
    print("UDP Server 1 running on port 9999...")

    while True:
        message, addr = server.recvfrom(1024)
        message = message.decode()
        clients.add(addr)
        print(f"UDP Server 1 received: {message} from {addr}")

        # Broadcast to all clients except sender
        for client_addr in clients:
            if client_addr != addr:
                try:
                    server.sendto(message.encode(), client_addr)
                except:
                    pass

        # Forward to Server 2
        try:
            s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s2.sendto(f"[FROM_S1]{message}".encode(), server2_addr)
        except:
            pass

threading.Thread(target=handle_messages).start()
