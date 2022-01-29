import random
import word_bank

def hangman():
    hidden_word = random_word(word_bank.word_bank)
    # print(hidden_word)
    initial_state = word_status(hidden_word)
    attempt_remaining = attempt_status()
    print(initial_state)
    print(attempt_remaining)
    print()

    guess_letter = prompt_user()

    # if guess_letter in 

    
    



def random_word(list):
    hidden_word = random.choice(list)

    return hidden_word


def word_status(word):
    initial_state = ""

    for character in word:
       initial_state += "_" 

    return initial_state


def attempt_status():
    for i in range(1, 7):
        if i == 1:
            return "Attempts remaining: X X X X X X"
        if i == 2:
            return "Attempts remaining: X X X X X "
        if i == 3:
            return "Attempts remaining: X X X X "
        if i == 4:
            return "Attempts remaining: X X X "
        if i == 5:
            return "Attempts remaining: X X "
        if i == 6:
            return "Attempts remaining: X "


def prompt_user():
    guess_letter = input("Guess a letter: ")

    return guess_letter

if __name__ == "__main__":
    hangman()