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

# Round-robin selection
servers = [9999, 8888]
client_number = int(input("Enter client number (1-4): "))
server_port = servers[(client_number - 1) % 2]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', server_port))

username = input("Enter your username: ")
print(f"Connected to Server on port {server_port}")

threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

while True:
    message = input("You: ")
    if message.lower() == 'exit':
        break
    client.send(f"{username}: {message}".encode())

client.close()
