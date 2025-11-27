import socket
import threading

def receive_tcp(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"\n{message}")
                print("You: ", end='', flush=True)
        except:
            break

def receive_udp(client_socket):
    while True:
        try:
            message, addr = client_socket.recvfrom(1024)
            print(f"\n{message.decode()}")
            print("You: ", end='', flush=True)
        except:
            break

print("=== Chatroom Client ===")
protocol = input("Select protocol (TCP/UDP): ").upper()
server_choice = input("Select server (1 or 2): ")
server_port = 9999 if server_choice == '1' else 8888
username = input("Enter your username: ")

if protocol == 'TCP':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', server_port))
    print(f"Connected via TCP to Server {server_choice}")

    threading.Thread(target=receive_tcp, args=(client,), daemon=True).start()

    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            break
        client.send(f"{username}: {message}".encode())

elif protocol == 'UDP':
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = ('localhost', server_port)
    client.sendto(b"JOIN", server_addr)
    print(f"Connected via UDP to Server {server_choice}")

    threading.Thread(target=receive_udp, args=(client,), daemon=True).start()

    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            break
        client.sendto(f"{username}: {message}".encode(), server_addr)

client.close()
print("Disconnected from chatroom")
