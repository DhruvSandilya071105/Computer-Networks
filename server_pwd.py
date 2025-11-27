import socket
import re

def validate_password(pwd):
    if len(pwd) < 8 or len(pwd) > 20:
        return "Invalid: Length must be 8-20 characters"
    if not re.search("[a-z]", pwd):
        return "Invalid: Must contain lowercase letter"
    if not re.search("[A-Z]", pwd):
        return "Invalid: Must contain uppercase letter"
    if not re.search("[0-9]", pwd):
        return "Invalid: Must contain digit"
    if not re.search("[_@$]", pwd):
        return "Invalid: Must contain _, @, or $"
    return "Valid password"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(1)
print("Password Validator server running on port 9999...")

while True:
    conn, addr = server.accept()
    print(f"Client {addr} connected")
    password = conn.recv(1024).decode()
    result = validate_password(password)
    conn.send(result.encode())
    print(f"Validated password from {addr}: {result}")
    conn.close()
