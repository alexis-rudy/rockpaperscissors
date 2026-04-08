import socket

# Create communication endpoint
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attaches server to specified local host address and port number
server.bind(('localhost', 8080))
# Server is waiting for incoming connections
server.listen()

print("Server waiting for connections...")

# Accept a connection from a client and print the client's address
conn, addr = server.accept()
print("Connected to: ", addr)

while True:
    # Connection is established, receive data from client (up to 1024 bytes) and decode it
    data = conn.recv(1024).decode()

    if not data:
        break

    print("Client: ", data)
    # Send response back to client
    conn.send(data.encode())

# Close the connection
conn.close()