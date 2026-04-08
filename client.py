import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect (("localhost", 8080))

while True:
    message = input("You: ")
    client.send(message.encode())

    response = client.recv(1024).decode()
    print("Server: ", response)