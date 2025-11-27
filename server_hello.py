import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(1)
print("Server listening on port 9999...")

conn, addr = server.accept()
print(f"Client connected: {addr}")
data = conn.recv(1024).decode()
print(f"Received: {data}")
conn.send("Hi Client, How are you?".encode())
conn.close()
server.close()
