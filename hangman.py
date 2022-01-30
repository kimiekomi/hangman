import random
import word_bank

def hangman():
    hidden_word = random_word(word_bank.word_bank)
    print(hidden_word)
    word_state = word_status(hidden_word)
    attempt_remaining = 6
    attempt_state = attempt_status(attempt_remaining)

    print(word_state)
    print(attempt_state)
    print()

    new_state = ""

    for i in range(6):
        guess_letter = prompt_user()

        if not guess_letter.isalpha():
            print("Enter a valid letter")
            continue
    
        new_state = letter_compare(hidden_word, guess_letter)

        print(new_state)
        continue



    





def random_word(list):
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
    guess_letter = input("Guess a letter: ")

    return guess_letter


def letter_compare(string, letter):
    new_state = ""
    for i in range(len(string)):
        if letter in string[i]:
            new_state += letter.upper()
        else:
            new_state += "_"

    return new_state

if __name__ == "__main__":
    hangman()