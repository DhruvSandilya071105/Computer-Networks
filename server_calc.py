import socket
import threading

def handle_client(conn, addr):
    print(f"Client {addr} connected")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            num1, operator, num2 = data.split()
            num1, num2 = float(num1), float(num2)

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            else:
                result = "Invalid operator"

            conn.send(str(result).encode())
        except Exception as e:
            conn.send(f"Error: {str(e)}".encode())
            break
    conn.close()
    print(f"Client {addr} disconnected")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(2)
print("Calculator server running on port 9999...")

while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()
