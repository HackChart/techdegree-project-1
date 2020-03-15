"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    solution = random.randint(1, 10)
    guess = None
    tries = 0
    print("""
    -------------------------------------
    Welcome to the Number Guessing Game!
    -------------------------------------
    """)
    while guess != solution:
        #Validate player guess
        while type(guess) != int: # TODO: RECHECK THIS
            try:    
                guess = int(input("Guess a number between 1 and 10: "))
            except ValueError:
                print("Please enter a numeric value!")
            else:
                if guess not in range(11):
                    print("Sorry, the number has to be between 1 and 10")
                    guess = None
        print(guess)

        #Determine guess location
        if guess > solution:
            print("It's Lower!")
        elif guess < solution:
            print("It's Higher!")
        else:
            print(f"That's correct! The number was {solution}!")
        tries += 1
        guess = None
    


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()