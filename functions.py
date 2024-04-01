import random

# List of words for the game
words = ["hangman", "python", "computer", "programming", "keyboard", "mouse", "monitor", "internet"]

def select_random_word():
    return random.choice(words)