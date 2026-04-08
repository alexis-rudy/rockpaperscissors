import socket

# Decide the winner between two moves.
def determine_winner(move1, move2):
    if move1 == move2:
        return "It's a tie!"

    elif (
        (move1 == "rock" and move2 == "scissors") or
        (move1 == "paper" and move2 == "rock") or
        (move1 == "scissors" and move2 == "paper")
    ):
        return "Player 1 wins!"

    else:
        return "Player 2 wins!"

# Create communication endpoint
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attaches server to specified local host address and port number
server.bind(('localhost', 8080))
# Server is waiting for incoming connections
server.listen()

print("Server waiting for connections...")

clients = []

while len(clients) < 2:
    conn, addr = server.accept()
    print("Connected to:", addr)
    clients.append(conn)

player1 = clients[0]
player2 = clients[1]

print("Both players connected! Let's play!")

while True:
    player1.send("Choose rock, paper, or scissors:".encode())
    player2.send("Choose rock, paper, or scissors:".encode())

    move1 = player1.recv(1024).decode().lower()
    move2 = player2.recv(1024).decode().lower()

    result = determine_winner(move1, move2)

    player1.send(result.encode())
    player2.send(result.encode())