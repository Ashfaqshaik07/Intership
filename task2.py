import random
def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")
    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")
    print(f"Congratulations! You guessed the correct number, {number_to_guess}, in {attempts} attempts.")
guessing_game()