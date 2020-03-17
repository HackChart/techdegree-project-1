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
    highscore = 0
    will_play_again = True
    while will_play_again:
        print("""
        -------------------------------------
        Welcome to the Number Guessing Game!
        -------------------------------------
        """)
        if highscore != 0:
            print(f"HIGHSCORE: {highscore}")
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
            tries += 1
            if guess > solution:
                print("It's Lower!")
                guess = None
            elif guess < solution:
                print("It's Higher!")
                guess = None
            else:
                print(f"That's correct! The number was {solution}!\nIt took you {tries} tries to guess the correct number!")
                if highscore == 0 or tries < highscore:
                    highscore = tries
                

                    

                accepted_answers = ["y", "n", "yes", "no"]
                will_play_again = None
                while will_play_again not in accepted_answers:
                    will_play_again = input("Would you like to play again? (y)es/(n)o: ").lower()
                    if will_play_again in accepted_answers:
                        if will_play_again == "n":
                            print("Thanks for playing! The game will now exit.")
                            print(f"Your HIGHSCORE was {highscore}") #TODO: Format highscore
                            will_play_again = False
                    else:
                        print("Please enter (y)es or (n)o\n")
            
        


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()