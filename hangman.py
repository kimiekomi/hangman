"""
Date Created: 01/29/22
By: M Lassiter
Description: recreation of the classic word-guessing game - Hangman. 

"""

import random
import word_bank

debug = False

def main():
    while True:
        print("\nLets Play Hangman!\n")
        hangman()

        play_again = input("Play again? (y/n)").lower()

        if play_again == "y":
            continue

        print("\nSee you next time!\n")
        break


def hangman():

    if debug: print(f"initialized hangman()")

    hidden_word = random_word(word_bank.word_bank)
    if debug: print(f"hidden_word - {hidden_word}")

    word_state = word_status(hidden_word)
    

    print(word_state)
    print()

    correct_letters = ""
    incorrect_letters = ""
    attempts_remaining = 6

    while True:
        letter_guessed = prompt_user()

        if letter_guessed in correct_letters or letter_guessed in incorrect_letters:
            print(f"You've already guessed '{letter_guessed}'\n")
            continue

        if letter_guessed in hidden_word :
            correct_letters += letter_guessed
        else:
            incorrect_letters += letter_guessed
            attempts_remaining -= 1

        new_state = letter_compare(hidden_word, correct_letters)
        attempt_state = attempt_status(attempts_remaining)

        print(new_state + "\n")
        print(attempt_state)
        print(f"Wrong guesses: '{incorrect_letters}'\n")

        if not "_" in new_state:
            print("You've guessed the word!")
            break

        if len(incorrect_letters) == 6:
            print(f"The word was '{hidden_word}'\n")
            break


def random_word(list):

    if debug: print(f"initialized random_word()")

    hidden_word = random.choice(list)
    print(hidden_word)
    if "-" in hidden_word:
        hidden_word = random.choice(list)

    if debug: print(f"hidden_word - {hidden_word}")

    return hidden_word


def word_status(word):
    word_state = ""

    for character in word:
       word_state += "_" 

    return word_state


def attempt_status(attempt_remaining):
    
        if attempt_remaining == 6:
            return """Attempts remaining: X X X X X X\n
        x----x
        |             
        |
        |
        |
        |
        """
        if attempt_remaining == 5:
            return """Attempts remaining: X X X X X\n
        x-------x
        |       |
        |       0
        |       
        |
        |
        """
        if attempt_remaining == 4:
            return """Attempts remaining: X X X X\n
        x-------x
        |       |
        |       0
        |       |
        |
        |
        """
        if attempt_remaining == 3:
            return """Attempts remaining: X X X \n
        x-------x
        |       |
        |       0
        |      /|
        |
        |
        """
        if attempt_remaining == 2:
            return """Attempts remaining: X X\n
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
        """
        if attempt_remaining == 1:
            return """Attempts remaining: X\n
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
        """
        else:
            return """Attempts remaining: None\n
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
        
        GAME OVER
            """


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

    if debug: print(f"guess_ letter - {guess_letter}")

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
    main()