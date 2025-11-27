import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

city = input("Enter city name (Mumbai/Delhi/Bangalore/Chennai/Kolkata): ")
client.send(city.encode())
weather_report = client.recv(1024).decode()
print(f"\nWeather Report for {city}:")
print(weather_report)

client.close()
