import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))
print("Connected to Calculator Server")

while True:
    num1 = input("Enter first number (or 'exit' to quit): ")
    if num1.lower() == 'exit':
        break

    operator = input("Enter operator (+, -, *, /): ")
    num2 = input("Enter second number: ")

    client.send(f"{num1} {operator} {num2}".encode())
    result = client.recv(1024).decode()
    print(f"Result: {result}\n")

client.close()
