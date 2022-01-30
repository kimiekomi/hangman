import random
import word_bank

debug = True

def hangman():
    hidden_word = random_word(word_bank.word_bank)
    print(hidden_word)

    attempt_remaining = 6
    word_state = word_status(hidden_word)
    attempt_state = attempt_status(attempt_remaining)

    print(word_state)
    print(attempt_state)
    print()

    new_state = ""
    guessed_letters = []

    for i in range(6):
        while True:
            guess_letter = prompt_user()

        new_state = letter_compare(hidden_word, guess_letter)
        guessed_letters.append(guess_letter)

    print(new_state)
        




    


def random_word(list):
    hidden_word = random.choice(list)

    if "-" in hidden_word:
        hidden_word = random.choice(list)

    return hidden_word


def word_status(word):
    word_state = ""

    for character in word:
       word_state += "_" 

    return word_state


def attempt_status(attempt_remaining):
    
        if attempt_remaining == 6:
            return "Attempts remaining: X X X X X X"
        if attempt_remaining == 5:
            return "Attempts remaining: X X X X X "
        if attempt_remaining == 4:
            return "Attempts remaining: X X X X "
        if attempt_remaining == 3:
            return "Attempts remaining: X X X "
        if attempt_remaining == 2:
            return "Attempts remaining: X X "
        if attempt_remaining == 1:
            return "Attempts remaining: X "


def prompt_user():

    while True: 
        guess_letter = input("Guess a letter: ")

        if not guess_letter.isalpha():
            print("Enter a valid letter")
            continue

        if len(guess_letter) > 1:
            print("Enter only one letter")
            continue

        break

    return guess_letter


def letter_compare(secret_word, correct_letters):

    if debug: print (f"letter_compare (secret_word={secret_word}, {correct_letters})")

    new_state = ""

    for letter in secret_word:

        if letter in correct_letters:
            new_state += letter.lower ()
        else:
            new_state += "_"

    if debug: print(f"new_state - {new_state}")

    return new_state


if __name__ == "__main__":
    hangman()