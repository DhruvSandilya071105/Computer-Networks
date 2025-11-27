import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

password = input("Enter password to validate: ")
client.send(password.encode())
response = client.recv(1024).decode()
print(f"\nValidation Result: {response}")

client.close()
