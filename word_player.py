import random


class WordPlayer:
    def __init__(self, name: str):
        self.name = name  # player's name
        self.total_score = 0  # Cumulative score
        self.current_score = 100  # The player's current score in a single game
        self.current_round = 0  # Number of guess rounds in a game
        self.hint = 2  # player have 2 chance to get a hint
        self.present_word = []  # Display the current situation of guess
        self.secret_word = []  # The word needs to be guessed

    # Reset the status for a new game
    def reset(self):
        self.current_score = 100
        self.current_round = 1
        self.hint = 2

    # store the word need to be guessed
    def set_secret_word(self, secret_word):
        self.secret_word = list(secret_word.lower())
        self.present_word = ["*"] * len(secret_word)

    # Check whether the current score is greater than zero. If the score reaches zero, the game is considered failed.
    def game_continue(self):
        if self.current_score > 0:
            return True
        else:
            return False

    # Get random hint
    def use_hint(self):
        if self.hint <= 0:
            print(f"No hints remaining. You've already used up your hints.")
        else:
            # Each hint cost 5 marks
            if self.current_score - 5 > 0:
                self.current_score -= 5
                # The hint should randomly come from unknown part
                unknown_list = []
                for i in range(len(self.present_word)):
                    if self.present_word[i] == '*':
                        unknown_list.append(i)
                random_index = random.choice(unknown_list)
                self.present_word[random_index] = self.secret_word[random_index]
                print(f"Letter {random_index + 1} is {self.present_word[random_index]}.")
                print("+", "-" * len(self.present_word), "+")
                print("|", "".join(self.present_word), "|")
                print("+", "-" * len(self.present_word), "+")
                self.hint -= 1
                print(f"You have {self.hint} hint(s) left.")
            # If current score - hint < 0, player cannot get the hint
            else:
                print("You’re too low on score to afford a hint.")
        self.current_round += 1

    # The beginning instruction
    def game_instruction(self):
        tips = [
            "Every wrong guess costs you 10 points!",
            "You have TWO hints — each one costs 5 points.",
            "Once you're out of points, it's GAME OVER!",
            "Guess the secret word before your score hits ZERO."
        ]
        length = 0
        for tip in tips:
            if length < len(tip):
                length = len(tip)
        print("+", "-" * (length + 2), "+", sep="")
        for tip in tips:
            print("|", tip.ljust(length), "|")
        print("+", "-" * (length + 2), "+", sep="")

    def guess_word(self):
        self.reset()
        print(f"🔢 The secret word has {len(self.secret_word)} letters.")
        self.game_instruction()
        while self.game_continue():
            print(f"🔁 Round: {self.current_round}")
            attempt = input("Please enter your guess or enter 'hint' for a hint (-5 points): ").lower()
            if attempt == "hint":
                self.use_hint()
                # If the word is gotten after use hint
                if "".join(self.present_word) == "".join(self.secret_word):
                    print("You get the answer!")
                    print(f"Final score: {self.current_score}")
                    self.total_score += self.current_score
                    return True
                else:
                    print(f"Score after hint: {self.current_score}\n")
                    # Jump out current loop
                    continue
            # If the length of input is not equal to secret word
            elif len(attempt) != len(self.secret_word):
                print(f"Your guess should be {len(self.secret_word)} letters long.")
                print(f"Current score: {self.current_score}\n")
                self.current_round += 1
            # The player get the secret word, jump out the loop
            elif attempt == "".join(self.secret_word):
                print("You get the answer!")
                print(f"Final score: {self.current_score}")
                self.total_score += self.current_score
                return True
            # Player's input doesn't equal to correct answer, mark -10
            else:
                for i in range(len(self.secret_word)):
                    if self.secret_word[i] == attempt[i]:
                        self.present_word[i] = self.secret_word[i]
                print("+", "-" * len(self.present_word), "+")
                print("|", "".join(self.present_word), "|")
                print("+", "-" * len(self.present_word), "+")
                # If the score minors 10 will become negative
                if self.current_score - 10 <= 0:
                    self.current_score = 0
                else:
                    self.current_score -= 10
                self.current_round += 1
                print(f"Current score: {self.current_score}\n")
        # When score = 0, jump out the loop and player lose the game
        print(f"💀 GAME IS OVER. You are out of attempts. The correct word is:", "".join(self.secret_word))
        return False


if __name__ == "__main__":
    player = WordPlayer("Bob")
    guess_word = "apple"
    player.set_secret_word(guess_word)
    success = player.guess_word()
