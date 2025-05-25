"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie - Bulls and Cows

author: Kateřina Stanevová
email: KStanevova@seznam.cz
"""

import random
import time


"""TODO Generate a random 4-digit number with unique digits, allowing zero except in the first position."""
def generate_secret_number():
    digits = list(range(10))
    first_digit = random.choice(digits[1:])  
    digits.remove(first_digit)  
    remaining_digits = random.sample(digits, 3)  
    secret_number = [first_digit] + remaining_digits
    return ''.join(map(str, secret_number))


"""TODO: Validate the user's guess by checking its length, uniqueness, format, and ensuring the first digit is not zero."""
def validate_guess(guess):
    if len(guess) != 4:
        return "The number must have exactly 4 digits."
    if not guess.isdigit():
        return "The number must contain only digits."
    if guess.startswith("0"):
        return "The number must not start with a zero."
    if len(set(guess)) != 4:
        return "The number must not contain duplicate digits."
    return None


 """TODO Compare the user's guess to the secret number and return the number of bulls and cows."""
def evaluate_guess(secret_number, user_guess):
    bulls = sum(secret_digit == guess_digit for secret_digit, guess_digit in zip(secret_number, user_guess))
    cows = sum(guess_digit in secret_number for guess_digit in user_guess) - bulls
    return bulls, cows


"""TODO Display a welcome message and game instructions."""
def print_welcome_message():
    separator = "-" * 47
    message = (
        f"Hi there!\n"
        f"{separator}\n"
        f"I've generated a random 4-digit number for you.\n"
        f"Let's play a Bulls and Cows game.\n"
        f"{separator}"
    )
    print(message)


"""TODO: Run the Bulls and Cows game by initializing the secret number, tracking the number of attempts,
validating user input, and providing feedback. The game continues until the user correctly guesses
the secret number, after which the total time taken and number of attempts are displayed."""
def play_game():
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
