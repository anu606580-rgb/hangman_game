"""
Hangman Game — CodeAlpha Task 1
Author: Intern
"""

import random

# Predefined word list
WORDS = ["python", "hangman", "laptop", "jungle", "rocket","printer"]

HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]


def display_state(wrong_guesses, guessed_letters, word):
    print(HANGMAN_STAGES[len(wrong_guesses)])
    print("\nWord: ", end="")
    for letter in word:
        print(letter if letter in guessed_letters else "_", end=" ")
    print()
    print(f"\nWrong guesses ({len(wrong_guesses)}/6): {', '.join(wrong_guesses) or 'None'}")


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = []

    print("=" * 40)
    print("       Welcome to HANGMAN!")
    print("=" * 40)
    print(f"The word has {len(word)} letters. You have 6 attempts.\n")

    while len(wrong_guesses) < 6:
        display_state(wrong_guesses, guessed_letters, word)

        # Check win
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 You won! The word was '{word}'.")
            return

        guess = input("\nGuess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠  Please enter a single alphabetic letter.")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print("⚠  You already guessed that letter!")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print(f"✅ Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses.append(guess)
            print(f"❌ Wrong! '{guess}' is not in the word.")

    # Game over
    display_state(wrong_guesses, guessed_letters, word)
    print(f"\n💀 Game over! The word was '{word}'.")


def main():
    while True:
        play_hangman()
        again = input("\nPlay again? (yes/no): ").lower().strip()
        if again not in ("yes", "y"):
            print("\nThanks for playing! Goodbye! 👋")
            break


if __name__ == "__main__":
    main()
