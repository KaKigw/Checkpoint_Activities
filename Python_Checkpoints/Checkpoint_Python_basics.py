""" Description: 

Guess the Number is a single-player game where the player is prompted to guess a number between 1 and 100. The game provides feedback to the player if their guess is too high or too low until they correctly guess the number.

Example :

Welcome to the Guess the Number game!
I'm thinking of a number between 1 and 100. Can you guess what it is?
Enter your guess: 50
Your guess is too high. Guess again.
Enter your guess: 25
Your guess is too low. Guess again.
Enter your guess: 37

Your guess is too high. Guess again.

Enter your guess: 31

Congratulations! You guessed the number correctly!

 


Instructions
 

Use the 'input' function to prompt the player to enter their guess as a string.
Use the 'int' function to convert the player's guess to an integer.
Use the 'import' statement to import the 'random' module.
Use the 'random.randint()' function to generate a random integer between 1 and 100.
Use an 'if/else' statement to check if the player's guess is too high, too low, or correct.
Use the 'print' function to provide feedback to the player based on their guess.
Use a 'while' loop to continue prompting the player for guesses until they correctly guess the number.
Note: 

The game can be customized to allow the player to choose the range of numbers or the number of guesses they are allowed before they lose the game. """
#Guess the Number Game
Guessed_Num = int(input("Welcome to the Guess the Number game!\nI'm thinking of a number between 1 and 100. Can you guess what it is?"))
Max_Guesses = int(input("What number of guesses do you allow yourself to guess before losing the game? "))
Num_Guesses = 1  # Initialize the number of guesses
import random
Random_Num = random.randint(1, 100)  # Generate a random number between 1 and 100
if Guessed_Num < Random_Num:
    print("Your guess is too low. Guess again.")
elif Guessed_Num > Random_Num:
    print("Your guess is too high. Guess again.")
else:
    print("Congratulations! You guessed the number correctly!")
while Guessed_Num != Random_Num:
    Guessed_Num = int(input("Enter your guess: "))
    if Guessed_Num < Random_Num:
        print("Your guess is too low. Guess again.")
    elif Guessed_Num > Random_Num:
        print("Your guess is too high. Guess again.")
    else:
        print("Congratulations! You guessed the number correctly!")
    Num_Guesses += 1  # Increment the number of guesses
    if Num_Guesses >= Max_Guesses:
        print(f"Sorry, you've used all {Max_Guesses} guesses. The number was {Random_Num}.")
        break


