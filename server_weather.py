import socket

weather_db = {
    "Mumbai": {"temp": "32°C", "humidity": "75%", "condition": "Humid"},
    "Delhi": {"temp": "28°C", "humidity": "60%", "condition": "Clear"},
    "Bangalore": {"temp": "25°C", "humidity": "65%", "condition": "Pleasant"},
    "Chennai": {"temp": "33°C", "humidity": "80%", "condition": "Hot and Humid"},
    "Kolkata": {"temp": "30°C", "humidity": "70%", "condition": "Cloudy"}
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(1)
print("Weather Service server running on port 9999...")

while True:
    conn, addr = server.accept()
    print(f"Client {addr} connected")
    city = conn.recv(1024).decode()

    if city in weather_db:
        data = weather_db[city]
        response = f"Temperature: {data['temp']}, Humidity: {data['humidity']}, Condition: {data['condition']}"
    else:
        response = "City not found in database"

    conn.send(response.encode())
    print(f"Sent weather data for {city} to {addr}")
    conn.close()
