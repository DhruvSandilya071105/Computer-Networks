# Computer-Networks
## Socket Programming - All Weeks (4-8)

Complete collection of client-server socket programming examples covering TCP, UDP, threading, and distributed systems.

## Directory Structure

```
socket_programming_all_weeks/
├── Week_4_Basic_Hello/
│   ├── server.py
│   └── client.py
├── Week_5_Calculator/
│   ├── server.py
│   └── client.py
├── Week_5_Password_Validator/
│   ├── server.py
│   └── client.py
├── Week_6_Echo_Server/
│   ├── server.py
│   └── client.py
├── Week_6_Weather_Service/
│   ├── server.py
│   └── client.py
├── Week_7_Distributed_Chatroom/
│   ├── server1.py
│   ├── server2.py
│   ├── client1.py
│   ├── client2.py
│   ├── client3.py
│   ├── client4.py
│   └── client_roundrobin.py
├── Week_8_TCP_UDP_Chatroom/
│   ├── server1_tcp.py
│   ├── server2_tcp.py
│   ├── server1_udp.py
│   ├── server2_udp.py
│   ├── client_tcp.py
│   ├── client_udp.py
│   └── client_unified.py
└── README.md
```

## How to Run

### Basic Programs (Weeks 4-6)

1. Open two terminal windows
2. Terminal 1: Run the server
   ```bash
   python server.py
   ```
3. Terminal 2: Run the client
   ```bash
   python client.py
   ```

### Week 7 - Distributed Chatroom

1. Open 6 terminal windows
2. Terminal 1: `python server1.py`
3. Terminal 2: `python server2.py`
4. Terminal 3-6: Run clients
   ```bash
   python client1.py
   python client2.py
   python client3.py
   python client4.py
   ```

**Alternative:** Use round-robin client
```bash
python client_roundrobin.py
```

### Week 8 - TCP/UDP Chatroom

**For TCP Mode:**
1. Terminal 1: `python server1_tcp.py`
2. Terminal 2: `python server2_tcp.py`
3. Terminal 3+: `python client_tcp.py`

**For UDP Mode:**
1. Terminal 1: `python server1_udp.py`
2. Terminal 2: `python server2_udp.py`
3. Terminal 3+: `python client_udp.py`

**For Unified Client (Choose TCP/UDP at runtime):**
```bash
python client_unified.py
```

## Features by Week

### Week 4: Basic Hello Exchange
- Simple client-server communication
- TCP connection establishment
- Message exchange

### Week 5: Calculator & Password Validator
- **Calculator:** Multi-client support with threading, arithmetic operations
- **Password Validator:** Regex-based validation, security checks

### Week 6: Echo & Weather Service
- **Echo Server:** Real-time message echoing with concurrent clients
- **Weather Service:** Dictionary-based data lookup, query-response pattern

### Week 7: Distributed Chatroom
- 2 servers working together
- 4 clients distributed across servers
- Inter-server communication
- Broadcasting to all participants
- Round-robin server selection option

### Week 8: TCP/UDP Chatroom
- Supports both TCP and UDP protocols
- Distributed architecture (2 servers)
- Demonstrates protocol differences:
  - TCP: Reliable, ordered delivery
  - UDP: Fast, connectionless (possible message loss)
- Unified client for protocol selection

## Exam Tips

### Time Management
1. **2 min:** Write basic socket structure
2. **5 min:** Add core logic
3. **1 min:** Add error handling (if time permits)

### Essential Patterns to Remember

**TCP Server:**
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', PORT))
s.listen(N)
conn, addr = s.accept()
data = conn.recv(1024).decode()
conn.send(response.encode())
conn.close()
```

**TCP Client:**
```python
import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('localhost', PORT))
c.send(message.encode())
response = c.recv(1024).decode()
c.close()
```

**UDP Server:**
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', PORT))
data, addr = s.recvfrom(1024)
s.sendto(response.encode(), addr)
```

**UDP Client:**
```python
import socket
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c.sendto(message.encode(), ('localhost', PORT))
response, addr = c.recvfrom(1024)
```

**Threading (for multiple clients):**
```python
import threading
def handle_client(conn, addr):
    # client handling logic
threading.Thread(target=handle_client, args=(conn, addr)).start()
```

### Quick Decision Tree
- **Multiple clients?** → Use threading
- **Data validation?** → Use regex or if-else
- **Bidirectional communication?** → Server sends response
- **Connectionless?** → Use UDP (SOCK_DGRAM)
- **Reliable delivery?** → Use TCP (SOCK_STREAM)

## Common Port Numbers Used
- Server 1 Main: 9999
- Server 2 Main: 8888
- Inter-server 1→2: 9998
- Inter-server 2→1: 9997

## Requirements
- Python 3.x
- No external libraries required (uses standard library)

## Notes
- All programs use 'localhost' for local testing
- Buffer size is set to 1024 bytes
- Remember to run servers before clients
- Use Ctrl+C to stop servers
- Type 'exit' in clients to disconnect gracefully

## Troubleshooting
- **Port already in use:** Change PORT number in both server and client
- **Connection refused:** Ensure server is running first
- **Module not found:** All required modules are in Python standard library

---
Created for NITK Computer Networks Lab
Socket Programming Examples - Weeks 4-8
