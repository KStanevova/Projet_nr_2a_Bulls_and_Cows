"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie - Bulls and Cows

author: Kateřina Stanevová
email: KStanevova@seznam.cz
"""

import random
import time


def generate_secret_number():
    """TODO Generate a random 4-digit number where each digit is unique, chosen from 0-9, and the first digit cannot be zero."""
    digits = list(range(10))
    first_digit = random.choice(digits[1:])  
    digits.remove(first_digit)  
    remaining_digits = random.sample(digits, 3)  
    secret_number = [first_digit] + remaining_digits
    return ''.join(map(str, secret_number))


def validate_guess(guess):
    """TODO Validate the user's guess to ensure:
    - It has exactly 4 digits.
    - It contains only numerical digits.
    - The first digit is not zero.
    - All digits are unique.

    Returns an error message if invalid, otherwise returns None.
    """
    if len(guess) != 4:
        return "The number must have exactly 4 digits."
    if not guess.isdigit():
        return "The number must contain only digits."
    if guess.startswith("0"):
        return "The number must not start with a zero."
    if len(set(guess)) != 4:
        return "The number must not contain duplicate digits."
    return None


def evaluate_guess(secret_number, user_guess):
    """TODO Compare the user's guess with the secret number, calculating:
    - Bulls (correct digit in the correct position).
    - Cows (correct digit in the wrong position).

    Returns a tuple containing the count of bulls and cows.
    """
    bulls = sum(secret_digit == guess_digit for secret_digit, guess_digit in zip(secret_number, user_guess))
    cows = sum(guess_digit in secret_number for guess_digit in user_guess) - bulls
    return bulls, cows


def print_welcome_message():
    """TODO Display a welcome message and game instructions."""
    separator = "-" * 47
    message = (
        f"Hi there!\n"
        f"{separator}\n"
        f"I've generated a random 4-digit number for you.\n"
        f"Let's play a Bulls and Cows game.\n"
        f"{separator}"
    )
    print(message)


def play_game():
    """Starts and runs the Bulls and Cows game.

    The game flow:
    - Generates a secret 4-digit number.
    - Tracks the number of attempts.
    - Validates user input and provides feedback.
    - Continues until the correct number is guessed.
    - Displays the total attempts and time taken at the end.
    """
    print_welcome_message() 
    
    secret_number = generate_secret_number()
    start_time = time.time()
    attempts = 0

    while True:
        user_guess = input("Enter a number: ")
        validation_error = validate_guess(user_guess)

        if validation_error:
            print(validation_error)
            continue

        attempts += 1
        bulls, cows = evaluate_guess(secret_number, user_guess)

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
