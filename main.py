"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie - Bulls and Cows

author: Kateřina Stanevová
email: KStanevova@seznam.cz
"""

import random
import time


def generate_secret_number():
    """Generates a random 4-digit number with unique digits."""
    secret_number = random.sample(range(1, 10), 4)
    return ''.join(map(str, secret_number))


def validate_guess(guess):
    """Validates the user's guess."""
    if len(guess) != 4:
        return "The number must have exactly 4 digits."
    if not guess.isdigit():
        return "The number must contain only digits."
    if guess.startswith("0"):
        return "The number must not start with a zero."
    if len(set(guess)) != 4:
        return "The number must not contain duplicates."
    return None


def evaluate_guess(secret, guess):
    """Evaluates the guess and returns the number of bulls and cows."""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows


def print_welcome_message():
    """Prints the welcome message for the game."""
    # text = "I've generated a random 4 digit number for you."
    # length = len(text)
    # print(length)
    separator = "-" * 47
    message = (
        f"Hi there!\n"
        f"{separator}\n"
        f"I've generated a random 4 digit number for you.\n"
        f"Let's play a bulls and cows game.\n"
        f"{separator}"
    )
    print(message)

def play_game():
    """Main function to play the Bulls and Cows game."""
    print_welcome_message()

    secret_number = generate_secret_number()
    start_time = time.time()
    attempts = 0

    while True:
        guess = input("Enter a number: ")
        validation_error = validate_guess(guess)

        if validation_error:
            print(validation_error)
            continue

        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)

        print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")

        if bulls == 4:
            duration = time.time() - start_time
            minutes, seconds = divmod(duration, 60)
            print(
            f"That's amazing! You guessed the secret number {secret_number} "
            f"in {attempts} attempts and {int(minutes)} minutes {seconds:.2f} seconds."
            )

            break


if __name__ == "__main__":
    play_game()
