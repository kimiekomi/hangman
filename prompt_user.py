
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