import random

def get_random_number():
    return random.randint(1, 100)

def get_user_guess():
    return input("Please enter your guess (or type 'exit' to quit): ")

def validate_guess(guess):
    if guess.lower() == 'exit':
        return 'exit'
    try:
        return int(guess)
    except ValueError:
        return None

def give_feedback(guess, number_to_guess):
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess}!")

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = get_random_number()
    attempts = 0

    while True:
        guess_input = get_user_guess()
        validated = validate_guess(guess_input)

        if validated == 'exit':
            print("Thanks for playing! Goodbye!")
            break
        if validated is None:
            print("That's not a valid number. Please try again.")
            continue

        attempts += 1
        if validated == number_to_guess:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break
        else:
            give_feedback(validated, number_to_guess)