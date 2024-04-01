import random

# List of words for the game , you can modify it 
words = ["hangman", "python", "computer", "programming", "keyboard", "mouse", "monitor", "internet"]

def select_random_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()