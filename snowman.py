from random import randint

from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown", "tatanka", "hello", "banana"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[randint(0, len(WORDS) - 1)]


def is_valid_guess(guess):
    """Enhanced input validation."""
    return len(guess) == 1 and guess.isalpha()


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the game state."""
    print("=" * 40)
    print(STAGES[min(mistakes, len(STAGES) - 1)])
    print()

    display_word = " ".join([letter if letter in guessed_letters else
                             "_" for letter in secret_word])
    print(f"Word:  {display_word}")

    if guessed_letters:
        print(f"Known: {', '.join(sorted(guessed_letters))}")

    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print("=" * 40)
    print()


def is_word_guessed(secret_word, guessed_letters):
    """Check if word is fully guessed."""
    return all(letter in guessed_letters for letter in secret_word)


def play_game():
    """ Main game loop."""
    secret_word = get_random_word()
    guessed_letters = set()  # Use set for faster lookup
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("🌨️  Welcome to Snowman Meltdown! 🌨️")
    print("Guess the word before the snowman melts!\n")

    while mistakes < max_mistakes and not is_word_guessed(secret_word, guessed_letters):
        display_game_state(mistakes, secret_word, guessed_letters)

        while True:
            guess = input("Enter a letter: ").lower().strip()

            if not is_valid_guess(guess):
                print("❌ Please enter a SINGLE LETTER (a-z)!")
                continue

            if guess in guessed_letters:
                print("❌ You already guessed that letter!")
                continue

            break  # Valid guess

        guessed_letters.add(guess)

        if guess in secret_word:
            print("✅ Good guess!")
        else:
            mistakes += 1
            print("❌ Wrong! The snowman melts further...")

        print()

    display_game_state(mistakes, secret_word, guessed_letters)

    if is_word_guessed(secret_word, guessed_letters):
        print("🎉 Congratulations! You saved the snowman!")
        print(f"    The word was: {secret_word.upper()}")
    else:
        print("💔 Oh no! The snowman completely melted!")
        print(f"    The word was: {secret_word.upper()}")


def main():
    """main function with replay."""
    while True:
        play_game()
        print()

        replay = input("Play again? (y/n): ").lower().strip()
        if replay not in ['y', 'yes']:
            print("Thanks for playing! 👋")
            break
        print()


if __name__ == "__main__":
    main()
