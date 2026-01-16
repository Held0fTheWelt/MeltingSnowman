# game_logic.py

from random import randint
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the game state."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word)
    print("\n")


def is_word_guessed(secret_word, guessed_letters):
    """Return True if all letters in the secret word have been guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")
    # print("Secret word selected:", secret_word)  # Uncomment for testing

    while mistakes <= max_mistakes and not is_word_guessed(secret_word, guessed_letters):
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!\n")
        else:
            mistakes += 1
            print("Wrong guess! The snowman is melting...\n")

    display_game_state(min(mistakes, max_mistakes), secret_word, guessed_letters)

    if is_word_guessed(secret_word, guessed_letters):
        print("You saved the snowman! The word was:", secret_word)
    else:
        print("Oh no! The snowman melted. The word was:", secret_word)


if __name__ == "__main__":
    play_game()
