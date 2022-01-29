import random
import word_bank

def hangman():
    hidden_word = random_word(word_bank.word_bank)
    # print(hidden_word)
    initial_state = initial_status(hidden_word)
    print(initial_state)

    
    



def random_word(list):
    hidden_word = random.choice(list)

    return hidden_word


def initial_status(word):
    initial_state = ""

    for character in word:
       initial_state += "_" 

    return initial_state


def prompt_user():
    guess_letter = input("Guess a letter: ")

    return guess_letter

if __name__ == "__main__":
    hangman()