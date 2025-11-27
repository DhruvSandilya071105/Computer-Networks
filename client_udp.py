import socket
import threading

def receive_messages_udp(client_socket):
    while True:
        try:
            message, addr = client_socket.recvfrom(1024)
            print(f"\n{message.decode()}")
            print("You: ", end='', flush=True)
        except:
            break

server_choice = input("Select server (1 or 2): ")
server_port = 9999 if server_choice == '1' else 8888
server_addr = ('localhost', server_port)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"Connected to UDP Server {server_choice}")

# Register with server
client.sendto(b"JOIN", server_addr)

threading.Thread(target=receive_messages_udp, args=(client,), daemon=True).start()

username = input("Enter your username: ")
while True:
    message = input("You: ")
    if message.lower() == 'exit':
        break
    client.sendto(f"{username}: {message}".encode(), server_addr)

client.close()
