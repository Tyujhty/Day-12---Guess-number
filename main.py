#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

print(logo)
print("Welcome, try to guess the computer choice between 1 and 100.\nTwo levels of difficulties.\n    Good luck :)")

def computer_choice():
    '''Choose a random number'''
    return random.choice(range(1,100))

def choose_difficulties():
    number_lives = 0
    user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if user_choice == 'easy':
        number_lives = 10
    elif user_choice == 'hard':
        number_lives = 5

    return number_lives


random_number = computer_choice()
print(random_number)

number_lives = choose_difficulties()
print(number_lives)
