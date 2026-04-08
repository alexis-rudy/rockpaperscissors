
def play_game():
    print("Let's play Rock, Paper, Scissors!")
    player_1_choice = "Paper"
    player_2_choice = "Scissors"
    # print(f"P1 chose: {player_1_choice}")
    # print(f"P2 chose: {player_2_choice}")
    game_over = False

    while not game_over:
        if player_1_choice == player_2_choice:
            print("It's a tie!")
        elif (player_1_choice == "Rock" and player_2_choice == "Scissors") or \
            (player_1_choice == "Paper" and player_2_choice == "Rock") or \
            (player_1_choice == "Scissors" and player_2_choice == "Paper"):
            print("P1 wins!")
        else:    
            print("P2 wins!")
        game_over = True

def main():
    play_game()

if __name__ == "__main__":
    main()