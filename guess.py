import random

def guess_the_number_game():
    """A simple number guessing game."""
    # Generate a random number between 1 and 100 (inclusive)
    secret_number = random.randint(1, 100)
    guess = 0
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 100.")

    # Loop until the user guesses correctly
    while guess != secret_number:
        try:
            # Get user input and convert it to an integer
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Provide feedback on the guess
            if guess < secret_number:
                print("Too low, try again.\n")
            elif guess > secret_number:
                print("Too high, try again.\n")
        except ValueError:
            # Handle cases where the user enters non-integer input
            print("Invalid input. Please enter a whole number.")
        except Exception as e:
            # Handle other potential errors
            print(f"An unexpected error occurred: {e}")

    # This code executes once the while loop breaks (i.e., the guess is correct)
    print(f"\nCongratulations! You guessed the number {secret_number} in {attempts} attempts!")

# Run the game function
if __name__ == "__main__":
    guess_the_number_game()
