from random import randint
from art import logo

TURNS_OF_EASY = 10
TURNS_OF_HARD = 5

turns = 0
# Func for guess
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High!")
        return turns - 1
    elif guess < answer:
        print("Too Low! Keep guessing")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

# Func for difficulty i.e easy or hard
def set_difficulty():
    level = input("Choose a difficulty level, Type 'easy' or 'hard': ")
    if level == "easy":
        return TURNS_OF_EASY
    else:
        return TURNS_OF_HARD
def game():
    print(logo)
    # Choose no. 1 - 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100....")
    answer = randint(1, 100)
    print(f"Psssst, the correct answer is {answer}")

    turns = set_difficulty()

    # Keep repeating it, while loop
    guess = 0
    while guess != answer:
        print(f" You have {turns} remaining attempts to guess the number.")

        # Number guess -> for User
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, you lose!")
            return
        elif guess != answer:
            print("Guess again?")

# Number of guesses and reduce by 1

game()
