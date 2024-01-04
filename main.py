import random
from replit import clear 
from art import logo

def computer_choice():
    '''Choose a random number'''
    return random.choice(range(1,100))

def choose_difficulties():
    number_lives = 0
    user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    '''Determinate number of lives'''
    if user_choice == 'easy':
        number_lives = 10
    elif user_choice == 'hard':
        number_lives = 5
    
    print(f"You have {number_lives} attempts remainings to guess the number.")
    
    return number_lives

def compare_results(random_number, number_lives):
    while number_lives != 0:
        
        user_guess = int(input("Make a guess: "))
        result = ''
        if user_guess < random_number:
            result = "Too low."
        elif user_guess > random_number:
            result = 'Tow high.'
        else:
            play_again = input("Congratulations, you guess the number\nTry again? 'y' or 'n': ")
            if play_again == 'y':
                return True
            else:
                return False
            
        number_lives -= 1
        
        print(result)
        print(f"You have {number_lives} attempts remainings to guess the number.\nGuess again!")
    
    return False

def game():
    start = True
    while start is not False:
        clear()
        print(logo)
        print("Welcome, try to guess the computer's choice between 1 and 100.\nTwo levels of difficulties.\n    Good luck :)")
        
        random_number = computer_choice()

        number_lives = choose_difficulties()

        play_again = compare_results(random_number, number_lives)

        if not play_again:
            replay = input(f"Sorry, you didn't find the {random_number}.\nTry again? 'y' or 'n'").lower()
            if replay != 'y':
                print("Good bye :(")
                start = False
game()