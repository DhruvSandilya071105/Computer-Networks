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

server_choice = input("Select server (1 or 2): ")
server_port = 9999 if server_choice == '1' else 8888

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', server_port))
print(f"Connected to TCP Server {server_choice}")

threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

username = input("Enter your username: ")
while True:
    message = input("You: ")
    if message.lower() == 'exit':
        break
    client.send(f"{username}: {message}".encode())

client.close()
