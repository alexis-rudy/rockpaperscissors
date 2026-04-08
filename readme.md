# Rock Paper Scissors

This project is a simple Python rock-paper-scissors game built with sockets. The server waits for two players, sends each player a prompt, receives their move, and then decides the winner. The repository also includes a small standalone game prototype in `rpslogic.py`.

## Instructions for Build and Use

Steps to run the software:

1. Open two terminals in the project folder.
2. Start the server first with `python3 server.py`.
3. Start the first client with `python3 client.py`.
4. Start the second client with `python3 client.py`.

Instructions for using the software:

1. Wait until both clients connect to the server.
2. Each client will be prompted to choose rock, paper, or scissors.
3. Type your move in the client window and press Enter.
4. The server will send the result back to both players.

## Development Environment

To recreate the development environment, you need:

* Python 3
* The Python standard library only (`socket`, `threading`, and `curses`)

## Useful Websites to Learn More

I found these websites useful in developing this project:

* [Python `socket` documentation](https://docs.python.org/3/library/socket.html)
* [Python `threading` documentation](https://docs.python.org/3/library/threading.html)
* [Python `curses` documentation](https://docs.python.org/3/library/curses.html)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Clean up `client.py` so the move-selection flow is fully wired in
* [ ] Add input validation for invalid moves
* [ ] Add support for replaying multiple rounds
