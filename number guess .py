import random

def guessing_game():
    name = input("May I ask you for your name? ")
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200. Go ahead. Guess!")

    number_to_guess = random.randint(1, 200)
    max_tries = 6
    attempts = 0
    guessed_correctly = False

    while attempts < max_tries and not guessed_correctly:
        try:
            guess = int(input("Guess: "))
            attempts += 1

            if guess > number_to_guess:
                print("The guess of the number that you have entered is too high. Try again!")
            elif guess < number_to_guess:
                print("The guess of the number that you have entered is too low. Try again!")
            else:
                guessed_correctly = True
                print(f"Congratulations, {name}! You've guessed the number {number_to_guess}.")

        except ValueError:
            print("Invalid input. Please enter an integer.")

    if not guessed_correctly:
        print(f"Nope. The number I was thinking of was {number_to_guess}")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        guessing_game()
    else:
        print("Thanks for playing!")

guessing_game()

