import random


class SecretWord:
    def __init__(self):
        self.words = []
        self.filename = 'word.txt'

    # Load words from the file and store them in self.words
    def get_word(self):
        try:
            f = open(self.filename, 'r')  # Open the file for reading
            while True:
                line = f.readline().strip().lower()
                self.words.append(line)
                # Stop if the line is empty
                if line == '':
                    break
        # If the file is not found
        except FileNotFoundError:
            print("The file word.txt cannot be found!")

    # Return a random word from the loaded list
    def get_random_word(self):
        if self.words != []:
            return random.choice(self.words)
        else:
            return None


if __name__ == "__main__":
    word = SecretWord()
    word.get_word()
    print(word.get_random_word())
