import word_player
import secret_word
import number_player


# Validate the number of players (must be 2 or 3)
def valid_num_player():
    while True:
        try:
            num_players = int(input('How many players are playing? (2-3 players)\n'))
            if 2 <= num_players <= 3:
                return num_players
            else:
                print("The number of players should be limited to 2-3\n")
        except ValueError:
            print("Please put in a valid number.")


# Validate the number of rounds (must be 1 or 5)
def valid_num_round():
    while True:
        try:
            num_rounds = int(input('How many rounds would you like play? (1-5 rounds)\n'))
            if 1 <= num_rounds <= 5:
                return num_rounds
            else:
                print("The number of rounds should be limited to 1-5\n")
        except ValueError:
            print("Please put in a valid number.")


# Run the word guessing game
def word_game():
    print("\nWelcome to the word guess game!")

    # Load secret words from txt
    word_source = secret_word.SecretWord()
    word_source.get_word()
    # If there is no word, stop the game
    if word_source.words == []:
        print("Cannot start game: No words loaded.")
        return

    # Ask for the number of player
    num_players = valid_num_player()

    # Ask for the game round
    num_round = valid_num_round()

    # Get player names, create WordPlayer objects, and store them in a list
    players = []
    for i in range(num_players):
        name = input(f"Enter name for Word Player {i + 1}: ")
        if name == "":
            name = f"Word Player {i + 1}"
        each_player = word_player.WordPlayer(name)
        players.append(each_player)

    # play multiple rounds
    for i in range(num_round):
        # Each player takes a turn to guess a randomly selected word
        for each_player in players:
            print(f"\n🎮 {each_player.name}'s turn!")
            guess_word = word_source.get_random_word()  # Get a secret word for this player
            each_player.set_secret_word(guess_word)
            each_player.guess_word()

    # After all players have played, display their final scores
    print("\n🏁 End of the game")
    for each_player in players:
        print(f"{each_player.name}'s total score: {each_player.total_score}")

    # Determine the winner
    top_score = 0
    winners = []
    for each_player in players:
        if top_score <= each_player.total_score:
            top_score = each_player.total_score
    for each_player in players:
        if top_score == each_player.total_score:
            winners.append(each_player.name)

    # Show the winner
    if len(winners) == 1:
        print(f"🏆 {winners[0]} wins the game!\n")
    else:
        print(f"🤝 It's a tie: ", end="")
        i = 0
        while i < len(winners):
            if i == len(winners) - 1:
                print(winners[i])
                i += 1
            else:
                print(winners[i], end=", ")
                i += 1
        print()


# Run the number guess game
def number_game():
    print("\nWelcome to the number guess game!")

    # Ask for the number of player
    num_players = valid_num_player()

    # Ask for the game round
    num_round = valid_num_round()

    # Get player names, create NumberPlayer objects, and store them in a list
    players = []
    for i in range(num_players):
        name = input(f"Enter name for Number Player {i + 1}: ")
        if name == "":
            name = f"Number Player {i + 1}"
        players.append(name)

    # Create a NumberPlayer object
    player = number_player.NumberPlayer(players)

    # play multiple rounds
    for i in range(num_round):
        player.guess_number()

    # Show the player who lost the most
    player.loser()


# Main program loop
def main():
    print("Welcome to the Game Center!")
    while True:
        # Game menu
        print("1. Word Guessing Game")
        print("2. Number Trap Game")
        print("3. Exiting")
        choice = input("Choose your game (please input 1 or 2 or 3): ")
        if choice == "1":
            word_game()
        elif choice == "2":
            number_game()
        elif choice == "3":
            print("\nBye! See you next time.")
            break
        else:
            print("Invalid selection.\n")


if __name__ == "__main__":
    main()
