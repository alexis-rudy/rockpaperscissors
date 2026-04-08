import socket
import threading
import curses

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8080))

def receive_messages():
    while True:
        message = client.recv(1024).decode()
        if message:
            print("\nOther player: ", message)

threading.Thread(target=receive_messages, daemon=True).start()

while True:
    message = input("You: ")
    client.send(message.encode())

options = ["rock", "paper", "scissors"]
print("Choose your move:")

def choose_move(stdscr):
    curses.curs_set(0)
    current_option = 0

    while True:
        stdscr.clear()
        stdscr.addstr("Choose your move:\n\n")

        for i, option in enumerate(options):
            if i == current:
                stdscr.addstr(f"> {option}\n")
            else:
                stdscr.addstr(f"  {option}\n")

        key = stdscr.getch()

        if key == curses.KEY_UP:
            current = (current - 1) % len(options)

        elif key == curses.KEY_DOWN:
            current = (current + 1) % len(options)

        elif key == ord("\n"):
            return options[current]