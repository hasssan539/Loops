# Write a program that continues to ask for a number until the correct number is guessed.

correct_number = 50  # The correct number to guess

while True:
    guess = int(input("Guess the number: "))  # Ask the user to guess a number
    
    if guess == correct_number:
        print("Congratulations! You guessed the correct number.")
        break  # Exit the loop if the guess is correct
    else:
        print("Incorrect, try again.")
