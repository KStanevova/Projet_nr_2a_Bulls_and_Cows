"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Kateřina Stanevová
email: KStanevova@seznam.cz
"""

import random
import time

# TODO generuj náhodné 4 ciferné číslo bez opakování
def generate_secret_number():
    digits = list(range(1, 10))  # číslice 1-9
    random.shuffle(digits)
    secret_number = digits[:4]
    return ''.join(map(str, secret_number))

# TODO ověř, že uživatel zadal 4 ciferné číslo bez opakování
def validate_guess(guess):
    if len(guess) != 4:
        return "The number must have exactly 4 digits."

    if not guess.isdigit():
        return "The number must contain only digits."

    if guess[0] == '0':
        return "The number must not start with a zero."

    if len(set(guess)) != 4:
        return "The number must not contain duplicates."

    return None

# TODO vyhodnoť, kolik bulls a cows uživatel uhodl
def evaluate_guess(secret, guess):
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows

# TODO hlavní funkce hry
def play_game():
    separator = "-" * 47  # 47 znaků dlouhý separátor
    print(f"Hi there!\n"f"{separator}\n"f"I've generated a random 4 digit number for you.\n"f"Let's play a bulls and cows game.\n"f"{separator}")

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

        if bulls == 1:
            bull_text = "bull"
        else:
            bull_text = "bulls"

        if cows == 1:
            cow_text = "cow"
        else:
            cow_text = "cows"

        print(f"{bulls} {bull_text}, {cows} {cow_text}")

        if bulls == 4:
            end_time = time.time()
            duration = end_time - start_time
            print(f"That's amazing! You guessed the secret number {secret_number} in {attempts} attempts and {duration:.2f} seconds.")
            break

if __name__ == "__main__":
    play_game()

 

 

 