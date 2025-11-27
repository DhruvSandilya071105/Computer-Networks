import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"\n{message}")
                print("You: ", end='', flush=True)
        except:
            break

server_port = 8888  # Client 4 connects to Server 2
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', server_port))

username = input("Enter your username (Client 4): ")
print("Connected to Server 2. Type your messages below:")

threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

while True:
    message = input("You: ")
    if message.lower() == 'exit':
        break
    client.send(f"{username}: {message}".encode())

client.close()
