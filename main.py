# Hangman Game
# Author: Ellabou Tesnime

from functions import select_random_word, display_word

def hangman():
    word_to_guess = select_random_word()
    # List to store guessed letters
    guessed_letters = []
    # Count of incorrect guesses
    incorrect_guesses = 0
    # Maximum allowed incorrect guesses
    max_incorrect_guesses = 6 


    print("Welcome to Hangman!")
    print("Try to guess the word.")
    print("")

    while True:
        # Display the current state of the word with guessed letters
        print("\nWord to guess: ", display_word(word_to_guess, guessed_letters))
        # Get user input for a letter guess
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            # Check if the input is a single letter
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            # Check if the letter has already been guessed
            print("You already guessed that letter.")
            continue
        # Add the guessed letter to the list
        guessed_letters.append(guess)  
        
        if guess in word_to_guess:
            # Check if the guessed letter is in the word
            print("Correct!")
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1  # Increment incorrect guesses

        if incorrect_guesses >= max_incorrect_guesses:
            # Check if maximum incorrect guesses reached
            print("\nSorry, you've run out of guesses.")
            print("The word was:", word_to_guess)
            break

        if all(letter in guessed_letters for letter in word_to_guess):
            # Check if all letters in the word have been guessed
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()