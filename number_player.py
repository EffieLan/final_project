import random
from collections import Counter


class NumberPlayer:
    def __init__(self, players):
        self.players = players  # list of all players
        self.turn = 0  # which player's turn
        # Current guessing range
        self.low = 1
        self.high = 99
        # Bomb number
        self.num = 0
        # List of players who lost each round
        self.lose = []

    # Reset the game state for a new round
    def reset(self):
        self.low = 1
        self.high = 99
        self.num = 0
        self.turn = 0

    # Switch to the next player's turn
    def switch_turn(self):
        self.turn = (self.turn + 1) % len(self.players)

    # Return the name of the player whose turn it is
    def current_player(self):
        return self.players[self.turn]

    # One round of number guess game
    def guess_number(self):
        print(f"\n not to guess the secret number between {self.low}-{self.high}... or you LOSE!")
        self.num = random.randint(2, 98)  # Random choose secret number
        while True:
            player = self.current_player()
            print(f"\n🎮 {player}'s turn. Current range: [{self.low}, {self.high}]")
            try:
                guess = int(input("Enter your guess: "))
                # Check the guess is within the valid range
                if guess <= self.low or guess >= self.high:
                    print("Guess must be strictly within the current range.")
                    continue
                # Player hits the secret number and jump out the loop (lose)
                if guess == self.num:
                    print(f"{player} guessed the number {self.num} and LOST the game!")
                    # Record lose player
                    self.lose.append(player)
                    break
                # Adjust the guessing range based on the guess
                elif guess > self.num:
                    self.high = guess
                else:
                    self.low = guess
                # Move to next player
                self.switch_turn()
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        # Reset game state after a round ends
        self.reset()

    # Determine which player lost the most time
    def loser(self):
        # Count how many times each player lost
        counter = Counter(self.lose)  # dict
        max_lose = max(counter.values())  # Find the max loss count
        loser_list = []
        # Collect all players with the max number of losses
        for player, lose_count in counter.items():
            if lose_count == max_lose:
                loser_list.append(player)
        print(f"The player(s) who triggered the number bomb the most: {','.join(loser_list)}\n")
