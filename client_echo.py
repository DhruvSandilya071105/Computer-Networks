import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Echo: {message}")
        except:
            print("Connection closed")
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))
print("Connected to echo server. Type 'exit' to quit.")

# Start receiving thread
threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

while True:
    message = input("You: ")
    if message.lower() == 'exit':
        break
    client.send(message.encode())

client.close()
